from django.urls import path
from quizapp.views import home,result, q_question, progress, completed

app_name = "quizapp"
urlpatterns = [
    path("",home,name="home"),
    path("quiz-question/<int:categoryid>/",q_question,name="q_question"),
    path("result/",result,name="result"),
    path("progress/",progress,name="progress"),
    path("completed/",completed,name="completed"),
]
