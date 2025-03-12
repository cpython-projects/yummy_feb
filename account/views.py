from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import TemplateView


# Create your views here.
class UserLoginView(LoginView):
    ...