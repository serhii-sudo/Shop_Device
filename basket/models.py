
from django.db import models

from store.models import Product
from user.models import CustomUser


class Basket(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE) # удалился пользователь - удалилась его корзины!
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE) # удалился продукт - удалилась корзина!
    quantity  = models.SmallIntegerField(default=0) #  изначальное количество товаров в корзине по умолчанию равно 0
    timestamp = models.DateTimeField(auto_now_add=True) # добавление автоматически даты и времени, когда был добавлен товар

    def __str__(self):
        return (f'корзина для, {self.user.email} | продукт: {self.product.name} | цена: {self.product.price}'
                f'| количество: {self.quantity}')

    def sum(self):
        return self.product.price * self.quantity