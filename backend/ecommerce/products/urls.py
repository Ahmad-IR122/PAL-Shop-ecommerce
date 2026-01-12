from django.urls import path

from products.views import *

urlpatterns = [
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-detail/<int:pk>', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-delete/<int:pk>', CategoryDeleteAPIView.as_view(), name='category-delete'),
    path('category-update/<int:pk>', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('products-list/', ProductsListAPIView.as_view(), name='products-list'),
    path('products-detail/<int:pk>', ProductDetailAPIView.as_view(), name='products-detail'),
    path('products-create/', ProductCreateAPIView.as_view(), name='products-create'),
    path('products-delete/<int:pk>', ProductDeleteAPIView.as_view(), name='products-delete'),
    path('products-update/<int:pk>', ProductUpdateAPIView.as_view(), name='products-update'),

]