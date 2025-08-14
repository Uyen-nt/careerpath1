from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib import admin as django_admin

from users.models import CustomUser
from quiz_highschool.models import QuizHighschool
from quiz_university.models import QuizUniversity

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

        "hs_top": hs_top,
        "uni_top": uni_top,
    }
    return render(request, "admin/dashboard.html", {**admin_ctx, **ctx})