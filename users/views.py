from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
    register_form = RegisterForm()
    return render(request, 'users/register.html', {'form': register_form})


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'

