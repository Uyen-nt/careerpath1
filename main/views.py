# home/views.py
from django.shortcuts import render
from django.http import JsonResponse
from quiz_highschool.models import ResultFeedback

PAGE_SIZE = 6

def home(request):
    qs = (ResultFeedback.objects
          .filter(approved=True, is_public=True, rating__gte=3)  
          .select_related("user")
          .order_by("-rating", "-created_at"))
    top_reviews = list(qs[:PAGE_SIZE])
    has_more = qs.count() > PAGE_SIZE
    return render(request, "home.html", {
        "top_reviews": top_reviews,
        "has_more_reviews": has_more,
        "page_size": PAGE_SIZE,
    })


def reviews_load(request):
    offset = int(request.GET.get("offset", 0) or 0)
    qs = (ResultFeedback.objects
          .filter(approved=True, is_public=True, rating__gte=1)
          .select_related("user")
          .order_by("-rating", "-created_at"))

    items = [{
        "user": fb.masked_user,
        "rating": fb.rating,
        "comment": fb.comment or "(Không có nội dung)",
        "created": fb.created_at.strftime("%d/%m/%Y %H:%M"),
    } for fb in qs[offset: offset + PAGE_SIZE]]

    next_offset = offset + PAGE_SIZE if qs.count() > offset + PAGE_SIZE else None
    return JsonResponse({"items": items, "next_offset": next_offset})
