from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'text email', 'placeholder': 'Введите адрес эл. почты'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'text', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'text w3lpass', 'placeholder': 'Подтвердите пароль'})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class UserAuthorizationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'text email', 'placeholder': 'Введите адрес эл. почты'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'text', 'placeholder': 'Введите пароль'})
    )

    def clean(self):
        # Извлекаем email и пароль из очищенных данных формы
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Аутентификация пользователя
        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError('Неверное имя пользователя или пароль')

        # Сохраняем объект пользователя в cleaned_data
        self.cleaned_data['user'] = user
        return self.cleaned_data


