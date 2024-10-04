# get_object_or_404 — Эта функция вызывает данную модель и получает из нее объект,
# если этот объект или модель не существует, возникает ошибка 404.

from django.shortcuts import render, get_object_or_404
from django.views import View
from store.models import Category, Product


class MainCategory(View):
    template_path = 'store/home.html'

    def get(self, request):
        all_categories = Category.objects.all()
        return render(request, self.template_path, {'all_categories': all_categories})


class GetAllProductsByCategories(View):
    template_path = 'store/all_categories.html'

    def get(self, request, categories_name):
        categories = get_object_or_404(Category, name=categories_name)
        product_all = Product.objects.filter(categories=categories)
        return render(request, self.template_path, {'product_all': product_all})


