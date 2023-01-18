from django.urls import path
from quizapp.views import home,result, q_question

app_name = "quizapp"
urlpatterns = [
    path("",home,name="home"),
    path("quiz-question/<int:categoryid>/",q_question,name="q_question"),
    path("result/",result,name="result")
]
