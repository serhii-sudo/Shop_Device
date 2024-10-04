from django.contrib.auth.models import AbstractUser
from django.db import models

# Была проблема бд, не пропускала следующего юзера для регистрации, так как поле username ...= (unique = Tru)
# что бы решить проблему, пришлось дописать новое поле name, в котором, username = email
# что дало возможность идентифицировать юзера на уникальность по email


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):   # Переопределяем метод save, который вызывается при сохранении объекта модели
        if not self.username:    # Проверяем, если поле username пустое (None или пустая строка)
            self.username = self.email   # Автоматически устанавливаем значение поля username равным значению поля email
        super().save(*args, **kwargs)   # Вызываем метод save родительского класса AbstractUser, чтобы сохранить объект в базе данных