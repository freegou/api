from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from User.models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'value', 'code', 'price', 'description', 'search', 'images')

class UnitSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Unit
        fields = ('id', 'price', 'number', 'product')

class ShelfSerializer(serializers.ModelSerializer):
    shelf_units = UnitSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Shelf
        fields = ('id', 'shelf_units')
