from django.urls import path

from orders.views import CartDetailAPIView, AddToCartAPIView, RemoveFromCartAPIView, UpdateCartItemAPIView

urlpatterns = [
    path('cart/' , CartDetailAPIView.as_view(), name='cart_detail'),
    path('cart/add/',AddToCartAPIView.as_view() , name='add_to_cart'),
    path('cart/delete/<int:pk>/',RemoveFromCartAPIView.as_view() , name='remove_from_cart'),
    path('cart/update/<int:pk>/',UpdateCartItemAPIView.as_view(), name='update_item'),
]