from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import RegisterSerializer


# Create your views here.

class RegisterCustomerAPIView(APIView):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             user = serializer.save()
             customer_group, _ = Group.objects.get_or_create(name='Customer')
             user.groups.add(customer_group)
             refresh_token = RefreshToken.for_user(user)

             return Response({
                 "massage" : "User registered successfully",
                 "role" : "Customer",
                 "user" : {
                     "id" : user.id,
                     "username" : user.username,
                     "email" : user.email,
                 },
                 "token" : {
                     "refresh" : str(refresh_token),
                     "access" : str(refresh_token.access_token),
                 }
             },status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterSellerAPIView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post (self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Seller_group, _ = Group.objects.get_or_create(name='Seller')
            user.groups.add(Seller_group)
            refresh_token = RefreshToken.for_user(user)
            return Response({
                "message": "Seller registered successfully",
                "role": "Seller",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "tokens": {
                    "refresh": str(refresh_token),
                    "access": str(refresh_token.access_token),
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)