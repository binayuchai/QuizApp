from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from useraccount.forms import CustomerRegisterForm
from django.urls import reverse_lazy
# Create your views here.

User = get_user_model()
class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name="register.html"
    success_url = reverse_lazy("user:login")