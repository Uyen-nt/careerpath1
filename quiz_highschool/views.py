from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from collections import Counter
from .career_analysis_html import ANALYSIS_HTMLS
from .career_analysis_cards import ANALYSIS_CARDS_PRIMARY, ANALYSIS_CARDS_SECONDARY
from django.contrib.auth.decorators import login_required
from .models import QuizHighschool

import os
from django.conf import settings


def gioi_thieu(request):
    return render(request, 'gioi_thieu.html')

@login_required
def question_hs(request):
    return render(request, 'question_hs.html')

# Mỗi nhóm ngành tương ứng với một mã định danh
CLUSTERS = ["social", "business", "tech", "science", "health", "arts"]

# Danh sách 20 câu hỏi và các lựa chọn
QUESTION_BANK = [
    {
        "question": "Bạn yêu thích môn học nào nhất?",
        "options": [
            {"text": "<i class='fas fa-book-open'></i> Ngữ văn, Lịch sử, Địa lý", "clusters": ["social"]},
            {"text": "<i class='fas fa-laptop-code'></i> Tin học, Công nghệ", "clusters": ["tech"]},
            {"text": "<i class='fas fa-flask'></i> Toán học, Vật lý, Hóa học", "clusters": ["science"]},
            {"text": "<i class='fas fa-palette'></i> Mỹ thuật, Âm nhạc, Thiết kế", "clusters": ["arts"]},
            {"text": "<i class='fas fa-seedling'></i> Sinh học, GDCD, Tâm lý học", "clusters": ["health"]}
        ]
    },
    {
        "question": "Bạn thích kiểu công việc nào nhất?",
        "options": [
            {"text": "<i class='fas fa-comments'></i> Giao tiếp và xây dựng mối quan hệ", "clusters": ["social"]},
            {"text": "<i class='fas fa-code-branch'></i> Phân tích và giải quyết vấn đề kỹ thuật", "clusters": ["tech"]},
            {"text": "<i class='fas fa-microscope'></i> Nghiên cứu và khám phá kiến thức mới", "clusters": ["science"]},
            {"text": "<i class='fas fa-paint-brush'></i> Sáng tạo và thiết kế sản phẩm", "clusters": ["arts"]},
            {"text": "<i class='fas fa-hand-holding-heart'></i> Hỗ trợ và chăm sóc cộng đồng", "clusters": ["health"]},
            {"text": "<i class='fas fa-chalkboard-teacher'></i> Giảng dạy hoặc đào tạo", "clusters": ["business"]}
        ]
    },
    {
        "question": "Điều gì quan trọng nhất trong công việc lý tưởng của bạn?",
        "options": [
            {"text": "<i class='fas fa-hands-helping'></i> Tác động tích cực đến cộng đồng", "clusters": ["social", "health"]},
            {"text": "<i class='fas fa-bolt'></i> Được tự do sáng tạo", "clusters": ["arts"]},
            {"text": "<i class='fas fa-cogs'></i> Tư duy logic và phân tích", "clusters": ["science"]},
            {"text": "<i class='fas fa-chart-line'></i> Thành công tài chính", "clusters": ["business"]},
            {"text": "<i class='fas fa-lock'></i> Ổn định và an toàn lâu dài", "clusters": ["health"]},
            {"text": "<i class='fas fa-leaf'></i> Bảo vệ môi trường và bền vững", "clusters": ["social"]}
        ]
    },
    {
        "question": "Bạn muốn làm việc trong môi trường nào nhất?",
        "options": [
            {"text": "<i class='fas fa-briefcase'></i> Văn phòng chuyên nghiệp, năng động", "clusters": ["business"]},
            {"text": "<i class='fas fa-flask'></i> Phòng thí nghiệm hoặc nghiên cứu", "clusters": ["science"]},
            {"text": "<i class='fas fa-palette'></i> Studio sáng tạo hoặc không gian nghệ thuật", "clusters": ["arts"]},
            {"text": "<i class='fas fa-users'></i> Cộng đồng hoặc tổ chức xã hội", "clusters": ["social"]},
            {"text": "<i class='fas fa-laptop'></i> Làm việc từ xa với công nghệ", "clusters": ["tech"]},
            {"text": "<i class='fas fa-school'></i> Trường học hoặc cơ sở giáo dục", "clusters": ["social"]}
        ]
    },
    {
        "question": "Bạn muốn học kỹ năng nào nhất nếu có cơ hội?",
        "options": [
            {"text": "<i class='fas fa-user-tie'></i> Lãnh đạo và quản lý đội nhóm", "clusters": ["business"]},
            {"text": "<i class='fas fa-code'></i> Lập trình phần mềm", "clusters": ["tech"]},
            {"text": "<i class='fas fa-heartbeat'></i> Kỹ năng chăm sóc sức khỏe", "clusters": ["health"]},
            {"text": "<i class='fas fa-chart-bar'></i> Phân tích dữ liệu và thống kê", "clusters": ["science"]},
            {"text": "<i class='fas fa-paint-roller'></i> Thiết kế đồ họa hoặc sáng tạo nội dung", "clusters": ["arts"]},
            {"text": "<i class='fas fa-leaf'></i> Quản lý tài nguyên môi trường", "clusters": ["health"]}
        ]
    },
    {
        "question": "Bạn thường dành thời gian rảnh cho hoạt động nào?",
        "options": [
            {"text": "<i class='fas fa-book'></i> Đọc sách hoặc viết lách", "clusters": ["arts"]},
            {"text": "<i class='fas fa-gamepad'></i> Chơi game logic hoặc giải đố", "clusters": ["tech"]},
            {"text": "<i class='fas fa-hands'></i> Tham gia hoạt động tình nguyện", "clusters": ["social"]},
            {"text": "<i class='fas fa-running'></i> Thể thao hoặc chăm sóc sức khỏe", "clusters": ["health"]},
            {"text": "<i class='fas fa-seedling'></i> Làm vườn hoặc bảo vệ môi trường", "clusters": ["social"]},
            {"text": "<i class='fas fa-chalkboard'></i> Học tập hoặc chia sẻ kiến thức", "clusters": ["social"]}
        ]
    },
    {
        "question": "Bạn làm việc hiệu quả nhất trong tình huống nào?",
        "options": [
            {"text": "<i class='fas fa-bolt'></i> Dưới áp lực và thời hạn gấp", "clusters": ["business"]},
            {"text": "<i class='fas fa-cloud'></i> Trong môi trường thoải mái, không áp lực", "clusters": ["arts"]},
            {"text": "<i class='fas fa-check-circle'></i> Khi có mục tiêu và kế hoạch rõ ràng", "clusters": ["science"]},
            {"text": "<i class='fas fa-users'></i> Khi làm việc cùng đội nhóm hỗ trợ", "clusters": ["social"]},
            {"text": "<i class='fas fa-laptop'></i> Khi sử dụng công nghệ hiện đại", "clusters": ["tech"]},
            {"text": "<i class='fas fa-heartbeat'></i> Khi giúp đỡ người khác", "clusters": ["health"]}
        ]
    },
    {
        "question": "Bạn cảm thấy tự tin nhất khi làm gì?",
        "options": [
            {"text": "<i class='fas fa-vial'></i> Thực hiện thí nghiệm hoặc nghiên cứu", "clusters": ["science"]},
            {"text": "<i class='fas fa-code'></i> Viết mã hoặc phát triển phần mềm", "clusters": ["tech"]},
            {"text": "<i class='fas fa-comment-dots'></i> Thuyết trình hoặc giao tiếp", "clusters": ["social"]},
            {"text": "<i class='fas fa-paint-brush'></i> Tạo ra sản phẩm nghệ thuật", "clusters": ["arts"]},
            {"text": "<i class='fas fa-medkit'></i> Chăm sóc và hỗ trợ người khác", "clusters": ["health"]},
            {"text": "<i class='fas fa-chalkboard-teacher'></i> Giảng dạy hoặc hướng dẫn", "clusters": ["business"]}
        ]
    },
    {
        "question": "Bạn thường theo dõi nội dung gì trên mạng?",
        "options": [
            {"text": "<i class='fas fa-rocket'></i> Công nghệ và khoa học mới", "clusters": ["tech", "science"]},
            {"text": "<i class='fas fa-globe'></i> Các vấn đề xã hội và môi trường", "clusters": ["social", "tech"]},
            {"text": "<i class='fas fa-heart'></i> Sức khỏe và lối sống lành mạnh", "clusters": ["health"]},
            {"text": "<i class='fas fa-chart-bar'></i> Kinh doanh và đầu tư", "clusters": ["business"]},
            {"text": "<i class='fas fa-camera'></i> Nội dung sáng tạo và nghệ thuật", "clusters": ["arts"]},
            {"text": "<i class='fas fa-book'></i> Giáo dục và phương pháp học tập", "clusters": ["tech"]}
        ]
    },
    {
        "question": "Công việc tương lai của bạn nên phản ánh điều gì?",
        "options": [
            {"text": "<i class='fas fa-user'></i> Phong cách và cá tính riêng", "clusters": ["arts"]},
            {"text": "<i class='fas fa-briefcase'></i> Sự chuyên nghiệp và uy tín", "clusters": ["business"]},
            {"text": "<i class='fas fa-users'></i> Kết nối và hỗ trợ cộng đồng", "clusters": ["social"]},
            {"text": "<i class='fas fa-hand-holding-heart'></i> Giá trị nhân văn và chăm sóc", "clusters": ["health"]},
            {"text": "<i class='fas fa-flask'></i> Khám phá và nghiên cứu", "clusters": ["science"]},
            {"text": "<i class='fas fa-leaf'></i> Bền vững và bảo vệ môi trường", "clusters": ["health"]}
        ]
    },
    {
        "question": "Bạn thích sử dụng công cụ nào nhất trong công việc?",
        "options": [
            {"text": "<i class='fas fa-paint-roller'></i> Phần mềm thiết kế sáng tạo", "clusters": ["arts"]},
            {"text": "<i class='fas fa-database'></i> Công cụ lập trình hoặc phân tích dữ liệu", "clusters": ["tech"]},
            {"text": "<i class='fas fa-tasks'></i> Phần mềm quản lý dự án", "clusters": ["business"]},
            {"text": "<i class='fas fa-stethoscope'></i> Thiết bị y tế hoặc chăm sóc sức khỏe", "clusters": ["health"]},
            {"text": "<i class='fas fa-leaf'></i> Công cụ quản lý tài nguyên môi trường", "clusters": ["health"]},
            {"text": "<i class='fas fa-chalkboard'></i> Nền tảng giáo dục hoặc giảng dạy", "clusters": ["tech"]}
        ]
    },
    {
        "question": "Bạn muốn tham gia hoạt động nào nếu có cơ hội?",
        "options": [
            {"text": "<i class='fas fa-calendar-alt'></i> Tổ chức sự kiện cộng đồng", "clusters": ["social"]},
            {"text": "<i class='fas fa-laptop-code'></i> Phát triển ứng dụng hoặc website", "clusters": ["tech"]},
            {"text": "<i class='fas fa-microscope'></i> Nghiên cứu khoa học ứng dụng", "clusters": ["science"]},
            {"text": "<i class='fas fa-palette'></i> Sáng tác nghệ thuật hoặc triển lãm", "clusters": ["arts"]},
            {"text": "<i class='fas fa-medkit'></i> Hỗ trợ y tế hoặc chăm sóc cộng đồng", "clusters": ["health"]},
            {"text": "<i class='fas fa-leaf'></i> Dự án bảo vệ môi trường", "clusters": ["science"]}
        ]
    },
    {
        "question": "Bạn đánh giá cao giá trị nào nhất trong công việc?",
        "options": [
            {"text": "<i class='fas fa-lightbulb'></i> Sáng tạo và đổi mới", "clusters": ["arts", "tech"]},
            {"text": "<i class='fas fa-check-circle'></i> Độ chính xác và khoa học", "clusters": ["science"]},
            {"text": "<i class='fas fa-heart'></i> Lòng nhân ái và sự hỗ trợ", "clusters": ["health", "social"]},
            {"text": "<i class='fas fa-trophy'></i> Thành công và ảnh hưởng lớn", "clusters": ["business"]},
            {"text": "<i class='fas fa-leaf'></i> Bền vững và tác động môi trường", "clusters": ["business"]},
            {"text": "<i class='fas fa-book'></i> Chia sẻ tri thức và giáo dục", "clusters": ["business"]}
        ]
    },
    {
        "question": "Bạn thích làm việc theo phong cách nào?",
        "options": [
            {"text": "<i class='fas fa-users-cog'></i> Làm việc nhóm và hợp tác", "clusters": ["social"]},
            {"text": "<i class='fas fa-user'></i> Làm việc độc lập và tập trung", "clusters": ["science"]},
            {"text": "<i class='fas fa-sync-alt'></i> Kết hợp nhóm và cá nhân", "clusters": ["tech"]},
            {"text": "<i class='fas fa-user-tie'></i> Dẫn dắt và ra quyết định", "clusters": ["business"]},
            {"text": "<i class='fas fa-tools'></i> Tự do thử nghiệm và sáng tạo", "clusters": ["arts"]},
            {"text": "<i class='fas fa-chalkboard-teacher'></i> Hướng dẫn và đào tạo người khác", "clusters": ["health"]}
        ]
    },
    {
        "question": "Bạn muốn thử sức với lĩnh vực nào trong tương lai?",
        "options": [
            {"text": "<i class='fas fa-briefcase'></i> Kinh doanh hoặc khởi nghiệp", "clusters": ["business"]},
            {"text": "<i class='fas fa-desktop'></i> Công nghệ thông tin và AI", "clusters": ["tech"]},
            {"text": "<i class='fas fa-flask'></i> Nghiên cứu khoa học hoặc kỹ thuật", "clusters": ["science"]},
            {"text": "<i class='fas fa-user-md'></i> Y tế và chăm sóc sức khỏe", "clusters": ["health"]},
            {"text": "<i class='fas fa-palette'></i> Nghệ thuật và sáng tạo nội dung", "clusters": ["arts"]},
            {"text": "<i class='fas fa-leaf'></i> Môi trường và phát triển bền vững", "clusters": ["social"]}
        ]
    },
    {
        "question": "Điều gì thu hút bạn nhất khi chọn nghề nghiệp?",
        "options": [
            {"text": "<i class='fas fa-arrow-up'></i> Cơ hội thăng tiến và phát triển", "clusters": ["business"]},
            {"text": "<i class='fas fa-hands-helping'></i> Tác động tích cực đến xã hội", "clusters": ["social"]},
            {"text": "<i class='fas fa-book-reader'></i> Khám phá và học hỏi tri thức", "clusters": ["science"]},
            {"text": "<i class='fas fa-heart'></i> Chăm sóc sức khỏe và hạnh phúc", "clusters": ["health"]},
            {"text": "<i class='fas fa-leaf'></i> Bảo vệ môi trường và bền vững", "clusters": ["tech"]},
            {"text": "<i class='fas fa-chalkboard'></i> Giảng dạy và truyền cảm hứng", "clusters": ["arts"]}
        ]
    },
    {
        "question": "Bạn muốn được công nhận vì điều gì trong công việc?",
        "options": [
            {"text": "<i class='fas fa-lightbulb'></i> Ý tưởng sáng tạo đột phá", "clusters": ["arts"]},
            {"text": "<i class='fas fa-user-tie'></i> Khả năng lãnh đạo xuất sắc", "clusters": ["business"]},
            {"text": "<i class='fas fa-hand-holding-heart'></i> Đóng góp cho cộng đồng", "clusters": ["social"]},
            {"text": "<i class='fas fa-award'></i> Thành tựu khoa học hoặc kỹ thuật", "clusters": ["science"]},
            {"text": "<i class='fas fa-heartbeat'></i> Chăm sóc sức khỏe cộng đồng", "clusters": ["health"]},
            {"text": "<i class='fas fa-leaf'></i> Đóng góp cho môi trường bền vững", "clusters": ["tech"]}
        ]
    },
    {
        "question": "Bạn thích giải quyết vấn đề theo cách nào?",
        "options": [
            {"text": "<i class='fas fa-chart-bar'></i> Dựa trên dữ liệu và phân tích", "clusters": ["science"]},
            {"text": "<i class='fas fa-users'></i> Thảo luận nhóm và hợp tác", "clusters": ["social"]},
            {"text": "<i class='fas fa-paint-brush'></i> Sáng tạo và thử nghiệm ý tưởng", "clusters": ["arts"]},
            {"text": "<i class='fas fa-hand-holding-heart'></i> Hỗ trợ và đồng cảm", "clusters": ["health"]},
            {"text": "<i class='fas fa-cogs'></i> Xây dựng quy trình và hệ thống", "clusters": ["tech"]},
            {"text": "<i class='fas fa-chalkboard-teacher'></i> Dạy học và hướng dẫn", "clusters": ["business"]}
        ]
    },
    {
        "question": "Bạn muốn làm việc với đối tượng nào nhất?",
        "options": [
            {"text": "<i class='fas fa-handshake'></i> Khách hàng hoặc đối tác kinh doanh", "clusters": ["business"]},
            {"text": "<i class='fas fa-users'></i> Cộng đồng hoặc tổ chức xã hội", "clusters": ["social"]},
            {"text": "<i class='fas fa-database'></i> Dữ liệu, công nghệ hoặc hệ thống", "clusters": ["tech"]},
            {"text": "<i class='fas fa-user-md'></i> Bệnh nhân hoặc người cần hỗ trợ", "clusters": ["health"]},
            {"text": "<i class='fas fa-leaf'></i> Môi trường hoặc tài nguyên thiên nhiên", "clusters": ["health"]},
            {"text": "<i class='fas fa-chalkboard'></i> Học sinh hoặc người học", "clusters": ["science"]}
        ]
    },
    {
        "question": "Kỹ năng hiện tại của bạn thuộc lĩnh vực nào?",
        "options": [
            {"text": "<i class='fas fa-code'></i> Lập trình hoặc công nghệ", "clusters": ["tech"]},
            {"text": "<i class='fas fa-users'></i> Giao tiếp và làm việc nhóm", "clusters": ["social"]},
            {"text": "<i class='fas fa-flask'></i> Nghiên cứu hoặc phân tích khoa học", "clusters": ["science"]},
            {"text": "<i class='fas fa-paint-brush'></i> Sáng tạo nghệ thuật hoặc thiết kế", "clusters": ["arts"]},
            {"text": "<i class='fas fa-heartbeat'></i> Chăm sóc sức khỏe hoặc hỗ trợ", "clusters": ["health"]},
            {"text": "<i class='fas fa-chalkboard-teacher'></i> Giảng dạy hoặc đào tạo", "clusters": ["business"]}
        ]
    }
]   

CLUSTERS_MAP = {
    "social": "Giáo dục – Xã hội",
    "business": "Quản lý – Kinh doanh",
    "tech": "Công nghệ – Kỹ thuật",
    "science": "Khoa học Tự nhiên",
    "health": "Y tế – Sức khỏe",
    "arts": "Sáng tạo – Nghệ thuật"
}

def next_question(request):
    if request.method == "POST":
        data = json.loads(request.body)
        answers = data.get("answers", [])
        question_index = data.get("question_index", 0)

        if question_index < len(QUESTION_BANK):
            q = QUESTION_BANK[question_index]
            return JsonResponse({
                "question": q["question"],
                "options": [opt["text"] for opt in q["options"]]
            })
        else:
            return JsonResponse({"end": True})


@login_required
def calculate_result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        answers = data.get("answers", [])

        scores = Counter()

        for q_index, selected_indices in enumerate(answers):
            question = QUESTION_BANK[q_index]
            for idx in selected_indices:
                clusters = question["options"][idx]["clusters"]
                for cluster in clusters:
                    scores[cluster] += 1

        top_two = scores.most_common(2)
        first_code, first_score = top_two[0]
        second_code, second_score = top_two[1]

        total = sum(scores.values())
        if total:
            fp_raw = first_score / total * 100
            sp_raw = second_score / total * 100

            first_percentage = "{:.1f}".format(fp_raw).rstrip('0').rstrip('.')
            second_percentage = "{:.1f}".format(sp_raw).rstrip('0').rstrip('.')
        else:
            first_percentage = "0"
            second_percentage = "0"


        # Lưu kết quả vào database
        quiz_result = QuizHighschool.objects.create(
            user=request.user,
            answers=answers,
            cluster_percentages = {
            cluster: "{:.1f}".format(round(count / total * 100, 2)).replace(",", ".")
            for cluster, count in scores.items() },
            top_cluster_code=first_code,
            top_cluster_name=CLUSTERS_MAP[first_code],
            top_percentage=first_percentage,
            top_analysis_html=ANALYSIS_HTMLS[first_code].format(score=first_percentage),
            second_cluster_code=second_code,
            second_cluster_name=CLUSTERS_MAP[second_code],
            second_percentage=second_percentage,
            second_analysis_html=ANALYSIS_HTMLS[second_code].format(score=second_percentage),
        )

        # Lưu ID của kết quả vào session để truy xuất sau
        request.session['quiz_result_id'] = quiz_result.id

        return JsonResponse({"status": "ok", "redirect": "/quiz_highschool/ket-qua/"})



@login_required

def ket_qua(request):
    quiz_result_id = request.GET.get('quiz_id') or request.session.get('quiz_result_id')
    
    if quiz_result_id:
        try:
            quiz_result = QuizHighschool.objects.get(id=quiz_result_id, user=request.user)
            named_cluster_percentages = {
                CLUSTERS_MAP.get(cluster, cluster): percentage
                for cluster, percentage in quiz_result.cluster_percentages.items()
            }

            # ✅ Thêm vào đây để sắp xếp giảm dần
            named_cluster_percentages = dict(
                sorted(
                    named_cluster_percentages.items(),
                    key=lambda item: float(item[1]),
                    reverse=True
                )
            )

            # Kiểm tra ảnh tồn tại
            top_img_path = os.path.join(settings.BASE_DIR, 'static', 'images', f"{quiz_result.top_cluster_code}-amico.jpg")
            second_img_path = os.path.join(settings.BASE_DIR, 'static', 'images', f"{quiz_result.second_cluster_code}-amico.jpg")
            top_card_image_exists = os.path.exists(top_img_path)
            second_card_image_exists = os.path.exists(second_img_path)

            context = {
                "top_cluster_name": quiz_result.top_cluster_name,
                "top_cluster_code": quiz_result.top_cluster_code,         
                "top_percentage": quiz_result.top_percentage,
                "top_analysis_html": quiz_result.top_analysis_html,
                "top_card_html": ANALYSIS_CARDS_PRIMARY[quiz_result.top_cluster_code],
                "second_cluster_name": quiz_result.second_cluster_name,
                "second_cluster_code": quiz_result.second_cluster_code,   
                "second_percentage": quiz_result.second_percentage,
                "second_analysis_html": quiz_result.second_analysis_html,
                "second_card_html": ANALYSIS_CARDS_SECONDARY[quiz_result.second_cluster_code],
                "cluster_percentages": named_cluster_percentages,
                "top_card_image_exists": top_card_image_exists,
                "second_card_image_exists": second_card_image_exists,
            }

        except QuizHighschool.DoesNotExist:
            context = {
                "top_cluster_name": "Chưa có dữ liệu",
                "top_cluster_code": "none",
                "top_percentage": 0,
                "top_analysis_html": "<p>Bạn chưa hoàn thành bài test.</p>",
                "top_card_html": "",
                "second_cluster_name": "",
                "second_cluster_code": "none",
                "second_percentage": 0,
                "second_analysis_html": "",
                "second_card_html": "",
                "cluster_percentages": {},
                "top_card_image_exists": False,
                "second_card_image_exists": False,
            }
    else:
        context = {
            "top_cluster_name": "Chưa có dữ liệu",
            "top_cluster_code": "none",
            "top_percentage": 0,
            "top_analysis_html": "<p>Bạn chưa hoàn thành bài test.</p>",
            "top_card_html": "",
            "second_cluster_name": "",
            "second_cluster_code": "none",
            "second_percentage": 0,
            "second_analysis_html": "",
            "second_card_html": "",
            "cluster_percentages": {},
            "top_card_image_exists": False,
            "second_card_image_exists": False,
        }

    return render(request, 'ket_qua.html', context)





