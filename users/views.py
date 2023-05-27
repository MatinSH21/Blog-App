from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.instance.activate_account()
            register_form.save()
            messages.success(request, 'Account has been created! You can log into your account now.')
            return redirect('post-home')
    register_form = RegisterForm()
    return render(request, 'users/register.html', {'form': register_form})


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
