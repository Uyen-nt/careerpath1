from django.db import models
from django.conf import settings

class QuizHighschool(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_highschool_attempts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Lưu câu trả lời (20 câu, mỗi câu có thể chọn nhiều đáp án)
    answers = models.JSONField(default=list)

    # Lưu kết quả phần trăm mỗi nhóm ngành
    cluster_percentages = models.JSONField(default=dict)

    # Nhóm ngành phù hợp nhất
    top_cluster_code = models.CharField(max_length=20)
    top_cluster_name = models.CharField(max_length=100)
    top_percentage = models.FloatField()

    # Nhóm ngành phù hợp thứ 2
    second_cluster_code = models.CharField(max_length=20)
    second_cluster_name = models.CharField(max_length=100)
    second_percentage = models.FloatField()

    # Lưu sẵn bài phân tích HTML để hiển thị nhanh
    top_analysis_html = models.TextField()
    second_analysis_html = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.top_cluster_name} ({self.top_percentage}%)"
