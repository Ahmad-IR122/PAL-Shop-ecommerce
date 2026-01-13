from django.urls import path
from users.views import *
urlpatterns = [
path('api/auth/register/coustomer', RegisterCustomerAPIView.as_view()),
path('api/auth/register/seller', RegisterSellerAPIView.as_view()),
]