from django.urls import path
from quizapp.views import home,result

app_name = "quizapp"
urlpatterns = [
    path("",home,name="home"),
    path("submit-result/",result,name="result"),
]
