from django.contrib import admin

from store.models import Category, Product
from user.models import  CustomUser

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CustomUser)