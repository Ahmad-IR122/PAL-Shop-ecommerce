from rest_framework import serializers
from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'stock',
            'image',
            'image_url',
            'is_active',
            'category',
            'owner',
            'created_at',
        ]