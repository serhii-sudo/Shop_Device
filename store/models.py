from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=73)
    description = models.TextField(null=True, blank=True)  # blank=True определяет, будет ли поле обязательным в формах.
    image = models.ImageField(upload_to='image')  # автозагрузка с указанной директории
    price = models.DecimalField(decimal_places=3, max_digits=9)
    categories = models.ForeignKey(to=Category, on_delete=models.CASCADE)  # on_delete=models.PROTECT -в продакшн!

    def __str__(self):
        return f'{self.name} {self.price}'



