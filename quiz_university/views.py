from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils import timezone
import json
from collections import defaultdict

from .models import QuizUniversity
from .question_bank import QUESTION_BANKS
from django.views.decorators.http import require_POST
#from .analysis_generator import generate_analysis_html
from django.views.decorators.http import require_http_methods
from .generate_analysis_html import generate_analysis_html_social, generate_analysis_html_business, generate_analysis_html_tech, generate_analysis_html_health, generate_analysis_html_arts, generate_analysis_html_science, generate_detailed_analysis_html



def gioi_thieu(request):
    return render(request, 'gioi_thieu_u.html')

@login_required
@require_http_methods(["GET", "POST"])
def select_cluster(request):
    if request.method == "POST":
        try:
            selected_cluster_code = request.POST.get("selected_cluster_code")
            selected_cluster_name = request.POST.get("selected_cluster_name")

            if selected_cluster_code and selected_cluster_name:
                quiz = QuizUniversity.objects.create(
                    user=request.user,
                    selected_cluster_code=selected_cluster_code,
                    selected_cluster_name=selected_cluster_name
                )
                request.session['quiz_university_result_id'] = quiz.id
                request.session['selected_cluster_code'] = selected_cluster_code  # ✅ lưu nhóm ngành

                return redirect('quiz_university:question_u')  # Chuyển hướng đến trang câu hỏi
            else:
                return render(request, 'select_cluster_u.html', {
                    'error': 'Thiếu thông tin nhóm ngành.'
                })
        except Exception as e:
            return render(request, 'select_cluster_u.html', {
                'error': 'Dữ liệu không hợp lệ.'
            })
    
    # GET request: Hiển thị giao diện chọn nhóm ngành
    return render(request, 'select_cluster_u.html')

@login_required
def question_u(request):
    quiz_result_id = request.session.get('quiz_university_result_id')
    if not quiz_result_id or not QuizUniversity.objects.filter(id=quiz_result_id, user=request.user).exists():
        return redirect('quiz_university:select_cluster_u')
    return render(request, 'question_u.html')

@require_POST
@login_required
def next_question_u(request):
    data = json.loads(request.body)
    question_index = data.get("question_index", 0)

    cluster_code = request.session.get('selected_cluster_code')
    QUESTION_BANK = QUESTION_BANKS.get(cluster_code, [])

    if question_index < len(QUESTION_BANK):
        q = QUESTION_BANK[question_index]

        return JsonResponse({
            "question": q["question"],
            "options": q["options"]
        })
    else:
        return JsonResponse({"end": True})

@require_POST
@login_required
def submit_quiz_u(request):
    data = json.loads(request.body)
    answers = data.get("answers", [])

    cluster_code = request.session.get('selected_cluster_code')
    QUESTION_BANK = QUESTION_BANKS.get(cluster_code, [])

    if not isinstance(answers, list):
        return JsonResponse({"status": "error", "message": "Dữ liệu câu trả lời không hợp lệ."}, status=400)

    answers = answers[:len(QUESTION_BANK)]
    while len(answers) < len(QUESTION_BANK):
        answers.append([])

    category_scores = defaultdict(list)
    total_score = 0
    total_count = 0

    for idx, selected_list in enumerate(answers):
        if idx >= len(QUESTION_BANK):
            break
        q = QUESTION_BANK[idx]
        if not selected_list:
            continue
        avg_score = sum(selected_list) / len(selected_list)
        category_scores[q["category"]].append(avg_score)
        total_score += avg_score
        total_count += 1

    skill_scores = {
        category: round(sum(scores) / len(scores) * 100 / 4, 2)
        for category, scores in category_scores.items() if scores
    }
    readiness_score = round(total_score / total_count * 100 / 4, 2) if total_count else 0

    # ✅ Sửa ở đây:
    analysis_html = generate_analysis_html(cluster_code, skill_scores, readiness_score)
    detailed_analysis_html = generate_detailed_analysis_html(cluster_code, skill_scores, readiness_score)

    quiz_result_id = request.session.get('quiz_university_result_id')
    if not quiz_result_id:
        return JsonResponse({"status": "error", "message": "Không tìm thấy bài test."}, status=400)

    try:
        quiz_result = QuizUniversity.objects.get(id=quiz_result_id, user=request.user)
        quiz_result.answers = answers
        quiz_result.skill_scores = skill_scores
        quiz_result.readiness_score = readiness_score
        quiz_result.analysis_html = analysis_html
        quiz_result.detailed_analysis_html = detailed_analysis_html
        quiz_result.updated_at = timezone.now()
        quiz_result.save()
    except QuizUniversity.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Bài test không tồn tại."}, status=400)

    return JsonResponse({"status": "ok", "redirect": "/quiz_university/ket-qua/"})



# Đặt ở đầu views.py hoặc utils.py
def format_score(score):
    if score == int(score):
        return str(int(score))
    else:
        return f"{score:.1f}"

@login_required
def ket_qua_u(request):
    quiz_result_id = request.GET.get('quiz_id') or request.session.get('quiz_university_result_id')
    context = {}

    if quiz_result_id:
        try:
            quiz_result = QuizUniversity.objects.get(id=quiz_result_id, user=request.user)
            cluster_code = quiz_result.selected_cluster_code
            skill_scores = quiz_result.skill_scores
            readiness_score = quiz_result.readiness_score

            analysis_html = generate_analysis_html(cluster_code, skill_scores, readiness_score)
            detailed_analysis_html = generate_detailed_analysis_html(cluster_code, skill_scores, readiness_score)

            # ✅ Thêm định dạng hiển thị đẹp
            skill_scores_display = {k: format_score(v) for k, v in skill_scores.items()}
            readiness_score_display = format_score(readiness_score)

            context = {
                "selected_cluster_name": quiz_result.selected_cluster_name,
                "readiness_score": readiness_score_display,
                "skill_scores": skill_scores_display,
                "analysis_html": analysis_html,
                "detailed_analysis_html": detailed_analysis_html
            }
        except QuizUniversity.DoesNotExist:
            context = {"error": "Kết quả không tồn tại."}
    else:
        context = {"error": "Bạn chưa làm bài đánh giá."}

    return render(request, 'result_u.html', context)



def generate_analysis_html(cluster_code, skill_scores, readiness_score):
    cluster_mapping = {
        "social": generate_analysis_html_social,
        "business": generate_analysis_html_business,
        "tech": generate_analysis_html_tech,
        "health": generate_analysis_html_health,
        "arts": generate_analysis_html_arts,
        "science": generate_analysis_html_science,
    }
    try:
        func = cluster_mapping[cluster_code]
    except KeyError:
        raise ValueError(f"Invalid cluster_code: {cluster_code}")
    return func(skill_scores, readiness_score)




