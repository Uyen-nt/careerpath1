from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib import admin as django_admin

from users.models import CustomUser
from quiz_highschool.models import QuizHighschool
from quiz_university.models import QuizUniversity
import json
from datetime import datetime, time, timedelta
from django.utils import timezone

from premium.models import PremiumSubscription, Transaction
from collections import defaultdict


@staff_member_required
def admin_dashboard(request):
    admin_ctx = django_admin.site.each_context(request)

    now = timezone.now()
    start_7 = now - timedelta(days=7)

    # ===== KPIs =====
    total_users = CustomUser.objects.count()
    admin_count = CustomUser.objects.filter(is_staff=True).count()
    superadmin_count = CustomUser.objects.filter(is_superuser=True).count()
    signups_7d = CustomUser.objects.filter(date_joined__gte=start_7).count()

    # Users đã làm quiz
    hs_user_ids = set(QuizHighschool.objects.values_list('user_id', flat=True).distinct())
    uni_user_ids = set(QuizUniversity.objects.values_list('user_id', flat=True).distinct())
    both_users = hs_user_ids & uni_user_ids
    hs_only_users = hs_user_ids - uni_user_ids
    uni_only_users = uni_user_ids - hs_user_ids
    quiz_users = len(hs_user_ids | uni_user_ids)
    no_quiz = max(total_users - quiz_users, 0)
    quiz_rate = round((quiz_users / total_users) * 100, 1) if total_users else 0.0

    # Bar: Đăng ký 7 ngày gần đây
    labels_7, signups_series_7 = [], []
    for i in range(6, -1, -1):
        d = (now - timedelta(days=i)).date()
        labels_7.append(d.strftime("%d/%m"))
        signups_series_7.append(CustomUser.objects.filter(date_joined__date=d).count())

    # Donut: Tỉ lệ làm quiz (HS/SV)
    quiz_labels = ["Học sinh", "Sinh viên", "Cả hai", "Chưa làm"]
    quiz_values = [
        len(hs_only_users),
        len(uni_only_users),
        len(both_users),
        no_quiz,
    ]

    # (tuỳ chọn) top clusters
    hs_top = (QuizHighschool.objects.values("top_cluster_name")
            .annotate(n=Count("id")).order_by("-n")[:5])
    uni_top = (QuizUniversity.objects.values("selected_cluster_name")
            .annotate(n=Count("id")).order_by("-n")[:5])

    # ====== PREMIUM CHARTS (THÊM MỚI) ======

    # 1) Premium mới 7 ngày (theo ngày, chỉ tính giao dịch completed)
    days = 7
    start_30 = (now - timedelta(days=days-1)).date()  # bao gồm hôm nay
    # đếm theo ngày
    daily_map = defaultdict(int)
    qs_completed = Transaction.objects.filter(status='completed',
                                              created_at__date__gte=start_30)
    for row in (qs_completed
                .values('created_at__date')
                .annotate(n=Count('id'))
                .order_by('created_at__date')):
        daily_map[row['created_at__date']] = row['n']

    premium_labels_30, premium_series_30 = [], []
    for i in range(days-1, -1, -1):
        d = (now - timedelta(days=i)).date()
        premium_labels_30.append(d.strftime("%d/%m"))
        premium_series_30.append(daily_map.get(d, 0))

    # 2) Phân bổ gói Premium (theo months, chỉ tính completed)
    plan_rows = (Transaction.objects
                 .filter(status='completed')
                 .values('months')
                 .annotate(n=Count('id'))
                 .order_by('months'))
    plan_labels = [f"{r['months']} tháng" for r in plan_rows]
    plan_values = [r['n'] for r in plan_rows]

    # (khuyến nghị) Premium đang còn hiệu lực (để hiển thị KPI khác nếu muốn)
    premium_active_count = PremiumSubscription.objects.filter(
        subscription_end__gt=now
    ).count()

    # ===== JSON hoá cho Chart.js (kể cả các chart cũ, để template dùng *_json) =====
    labels_7_json = json.dumps(labels_7, ensure_ascii=False)
    signups_series_7_json = json.dumps(signups_series_7, ensure_ascii=False)
    quiz_labels_json = json.dumps(quiz_labels, ensure_ascii=False)
    quiz_values_json = json.dumps(quiz_values, ensure_ascii=False)

    premium_labels_30_json = json.dumps(premium_labels_30, ensure_ascii=False)
    premium_series_30_json = json.dumps(premium_series_30, ensure_ascii=False)
    plan_labels_json = json.dumps(plan_labels, ensure_ascii=False)
    plan_values_json = json.dumps(plan_values, ensure_ascii=False)

    ctx = {
        "total_users": total_users,
        "admin_count": admin_count,
        "superadmin_count": superadmin_count,
        "signups_7d": signups_7d,
        "quiz_users": quiz_users,
        "quiz_rate": quiz_rate,

        "labels_7": labels_7,
        "signups_series_7": signups_series_7,
        "quiz_labels": quiz_labels,
        "quiz_values": quiz_values,

        # ✅ thêm biến *_json để template lấy trực tiếp
        "labels_7_json": labels_7_json,
        "signups_series_7_json": signups_series_7_json,
        "quiz_labels_json": quiz_labels_json,
        "quiz_values_json": quiz_values_json,

        # ✅ PREMIUM charts
        "premium_labels_30_json": premium_labels_30_json,
        "premium_series_30_json": premium_series_30_json,
        "plan_labels_json": plan_labels_json,
        "plan_values_json": plan_values_json,

        # Nếu muốn dùng ở KPI khác
        "premium_active_count": premium_active_count,

        "hs_top": hs_top,
        "uni_top": uni_top,
    }
    return render(request, "admin/dashboard.html", {**admin_ctx, **ctx})