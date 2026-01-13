from django.urls import path
from users.views import *
urlpatterns = [
path('register/customer/', RegisterCustomerAPIView.as_view()),
path('register/seller/', RegisterSellerAPIView.as_view()),
]