from functools import total_ordering
from itertools import product

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from urllib3 import request

import user
from basket.models import Basket
from store.models import Product


class AddInBasket(View):  # добавление товара в корзину
    def post(self, request,  product_id):
        product = get_object_or_404(Product, id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)

        else:
            basket = baskets.first()
            basket.quantity+=1
            basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # страница, где было выполнено действие


class BasketView(View):
    template_patch = 'basket/basket.html'

    def get(self, request):
        basket_user = Basket.objects.filter(user=request.user)  # посмотреть содержимое корзины, продукция юзера
        count_product_basket = len(basket_user) # количество товаров в корзине

        sum_all_products = [i.product.price for i in basket_user]
        return render(request, self.template_patch, {'basket_product': basket_user,
                                                     'count_product_basket':  count_product_basket,
                                                     'sum_all_products': sum(sum_all_products)})


class DelBasket(View):
    def post(self, request, product_id):    # удаление товара из корзины
        basket = Basket.objects.get(pk=product_id)
        basket.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))







