from django.contrib import admin
from quizapp.models import QQuestion,Category,Answer


@admin.register(QQuestion)
class QQuestionAdmin(admin.ModelAdmin):
    list_display = ("title","category","created_at","modified_at")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category","created_at","modified_at")
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("title","question","is_correct","created_at","modified_at") 
       
    
    
    