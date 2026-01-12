from django.db import transaction
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import CartItem, Cart
from orders.serializers import *

# Create your views here.

class CartDetailAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,**kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddToCartAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,**kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )
        item.quantity += quantity
        item.save()

        return Response({
            'message': 'Item added to cart successfully',
        })

class RemoveFromCartAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request,**kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        item_id = request.data.get('item_id')
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        item.delete()

        return Response({"message": "Item removed from cart"})

class UpdateCartItemAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request,**kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        item_id = request.data.get('item_id')
        item = get_object_or_404(CartItem, id=item_id, cart=cart)

        quantity = int(request.data.get('quantity'))
        item.quantity = quantity
        item.save()

        return Response({"message": "Cart item updated"})


class CreateOrderAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self,request,**kwargs):
        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()

        if not items.exists():
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )
        total = 0
        order = Order.objects.create(user=request.user ,total_price=0)

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,  # snapshot
                quantity=item.quantity
            )
            total += item.product.price * item.quantity

        order.total_price = total
        order.save()

        items.delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,**kwargs):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,**kwargs):
        order = Order.objects.get(id=order_id, user=request.user)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class UpdateOrderStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_id):
        order = Order.objects.get(id=order_id)
        status_value = request.data.get('status')

        order.status = status_value
        order.save()

        return Response({"message": "Order status updated"})


class DeleteOrderAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.status != 'PENDING':
            raise PermissionDenied(
            "You can only delete orders with PENDING status."
            )
        instance.delete()
