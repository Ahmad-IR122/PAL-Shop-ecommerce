from django.urls import path

from orders.views import *

urlpatterns = [
    path('cart/' , CartDetailAPIView.as_view(), name='cart_detail'),
    path('cart/add/',AddToCartAPIView.as_view() , name='add_to_cart'),
    path('cart/item/<int:item_id>/delete/',RemoveFromCartAPIView.as_view() , name='cart-item-delete'),
    path('cart/item/<int:item_id>/update/',UpdateCartItemAPIView.as_view(), name='cart-item-update'),
    path('orders/create/', CreateOrderAPIView.as_view(), name='order-create'),
    path('orders/list/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/<int:order_id>/status/', UpdateOrderStatusAPIView.as_view(), name='order-status'),
]