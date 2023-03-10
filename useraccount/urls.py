from django.urls import path
from useraccount.views import CustomLoginView, CustomRegisterView
from django.contrib.auth.views import LogoutView

app_name="user"

urlpatterns = [
    path("login/",CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", CustomRegisterView.as_view(), name="register"),
]
