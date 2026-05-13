from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import View


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')