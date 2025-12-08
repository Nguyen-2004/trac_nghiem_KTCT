from django.contrib import admin
from .models import Exam, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4  # Số dòng câu trả lời mặc định hiển thị để nhập

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam')  # Hiển thị câu hỏi và bộ đề ở danh sách
    list_filter = ('exam',)  # Lọc theo bộ đề
    inlines = [AnswerInline]  # Cho phép nhập câu trả lời trực tiếp

admin.site.register(Exam)
admin.site.register(Question, QuestionAdmin)
