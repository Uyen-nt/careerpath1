# fetch_data.py (UPDATED FOR LAST 7 DAYS)

from django.core.management.base import BaseCommand
from trend.models import TopIndustry, IndustryTrend
from django.utils.timezone import now
from datetime import datetime, timedelta, timezone
from random import uniform
import requests
import time

class Command(BaseCommand):
    help = 'Fetch job market data from Adzuna API with pagination (last 7 days) and update DB'

    def handle(self, *args, **kwargs):
        app_id = '160494d1'  # Replace with your Adzuna app_id
        app_key = '2eda2224bd01a8ea513c42037d15ef98'  # Replace with your Adzuna app_key
        country_code = 'gb'
        base_url = f'https://api.adzuna.com/v1/api/jobs/{country_code}/search/'

        # ---- Define 7-day window: today and the 6 previous days ----
        today = now().date()
        start_dt = datetime.combine(today - timedelta(days=6), datetime.min.time(), tzinfo=timezone.utc)
        end_dt = datetime.combine(today, datetime.max.time(), tzinfo=timezone.utc)

        industry_counts = {}
        total_pages = 8  # For testing; adjust to 20+ when stable

        for page in range(1, total_pages + 1):
            url = base_url + str(page)
            params = {
                'app_id': app_id,
                'app_key': app_key,
                'results_per_page': 100,
                'content-type': 'application/json',
            }
            try:
                response = requests.get(url, params=params, timeout=30)
            except requests.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Request error on page {page}: {e}"))
                break

            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f"Failed to fetch page {page}, status: {response.status_code}"))
                break

            data = response.json()
            jobs = data.get('results', [])

            for job in jobs:
                # Filter by created timestamp within last 7 days
                created_raw = job.get('created')
                if not created_raw:
                    continue
                try:
                    created_dt = datetime.fromisoformat(created_raw.replace('Z', '+00:00'))
                except Exception:
                    continue

                if not (start_dt <= created_dt <= end_dt):
                    continue

                category = job.get('category', {}).get('label', 'Unknown')
                industry_counts[category] = industry_counts.get(category, 0) + 1

            time.sleep(1)  # be nice to the API

        ICON_MAPPING = {
            'Teaching Jobs': 'fa-solid fa-chalkboard-teacher',
            'Engineering Jobs': 'fa-solid fa-cogs',
            'Healthcare & Nursing Jobs': 'fa-solid fa-heart-pulse',
            'Trade & Construction Jobs': 'fa-solid fa-building',
            'Social work Jobs': 'fa-solid fa-handshake',
            'Logistics & Warehouse Jobs': 'fa-solid fa-warehouse',
            'IT Jobs': 'fa-solid fa-laptop-code',
            'Sales Jobs': 'fa-solid fa-chart-line',
        }

        # Update TopIndustry from last 7-day counts (top 8)
        for name, count in sorted(industry_counts.items(), key=lambda x: x[1], reverse=True)[:8]:
            icon_class = ICON_MAPPING.get(name, 'fa-solid fa-briefcase')
            TopIndustry.objects.update_or_create(
                name=name,
                defaults={'job_count': count, 'icon': icon_class}
            )

        # ---- Ensure IndustryTrend has exactly the last 7 consecutive days ----
        # Create (backfill) a record for each of the last 7 days if missing
        for i in range(0, 7):
            d = today - timedelta(days=i)
            if not IndustryTrend.objects.filter(record_date=d).exists():
                IndustryTrend.objects.create(
                    name=f"Trend ngày {d.strftime('%d/%m/%Y')}",
                    description="Mô tả tự động từ fetch_data (7 ngày gần nhất)",
                    trend_score=round(uniform(0.3, 1.0), 2),
                    job_growth=f"Tăng {round(uniform(5, 20), 2)}%/năm",
                    record_date=d
                )
                self.stdout.write(self.style.SUCCESS(f"Created new trend data for {d}"))
            else:
                self.stdout.write(self.style.WARNING(f"Data for {d} already exists. Skipping creation."))

        # ---- Clean up: keep exactly these last 7 days ----
        keep_dates = [today - timedelta(days=i) for i in range(0, 7)]
        deleted_count, _ = IndustryTrend.objects.exclude(record_date__in=keep_dates).delete()

        self.stdout.write(self.style.SUCCESS(f"Cleaned {deleted_count} old records, kept {len(keep_dates)} recent days."))
        self.stdout.write(self.style.SUCCESS('Successfully updated top industries and trends for the last 7 days.'))
