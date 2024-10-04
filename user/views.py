from django.contrib import auth
from django.contrib.auth import login, password_validation
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import LogoutView,  PasswordChangeView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from urllib3 import request

from user.forms import UserRegistrationForm, UserAuthorizationForm


class RegistrationUser(View):
    template_path = 'user/registration.html'

    def get(self, request):
        print(request)
        form = UserRegistrationForm()
        return render(request, self.template_path, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login == cache(что бы не было новой регистрации, данные с кэша)
            return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_path, {'form': form})


# 24. перенаправление в личный кабинет пользователя, если данные валидны
# 26. возвращает заново форму регистрации, если данные не корректны


class AuthorizationUser(View):
    template_patch = 'user/authorization.html'

    def get(self, request):
        form = UserAuthorizationForm()
        return render(request, self.template_patch, {'form': form})

    def post(self, request):
        form = UserAuthorizationForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('user')
            print(user)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
            return render(request, self.template_patch,
                          {'form': form, 'error_message': 'Неверное имя пользователя или пароль'})


class LogOut(LogoutView):   #
    next_page = reverse_lazy('home')     # Выводит пользователя из системы

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response



