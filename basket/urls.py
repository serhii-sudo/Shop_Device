from django.urls import path

from basket.views import AddInBasket, DelBasket, BasketView

urlpatterns = [
    path('add/<int:product_id>/', AddInBasket.as_view(), name='add_basket'),
    path('del/<int:product_id>/', DelBasket.as_view(), name='del_basket'),
    path('user_basket', BasketView.as_view(), name='basket'),
]

