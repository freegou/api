from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ( 'id', 'user', 'phone', 'role', 'company', 'createtime')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'card')

class CompanyDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()
    class Meta:
        model = UserProfile
        fields = ('user', 'role', 'phone', 'company', 'createtime')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'createtime', 'updatetime')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'value', 'code', 'price', 'description', 'search', 'images', 'createtime', 'updatetime', 'owner')

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'remarker', 'gps', 'shopid', 'createtime')

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'value', 'code', 'price', 'description', 'search', 'images', 'createtime', 'updatetime')

class UnitSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Unit
        fields = ( 'id', 'price', 'number', 'product', 'offset', 'length')

class LayerSerializer(serializers.ModelSerializer):
    shelf_units = UnitSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Layer
        fields =( 'id', 'layernumber', 'shelf_units')

class ShelfSerializer(serializers.ModelSerializer):
    shelf_layers = LayerSerializer(many=True, required=False, read_only=True)
    owner = ShopSerializer()
    class Meta:
        model = Shelf
        fields = ( 'id', 'shelfnumber', 'shelf_layers', 'owner')

class UnitAddSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Unit
        fields = ('id', 'price', 'number','product', 'offset', 'length', 'shop', 'layer')

class LayerAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ('id', 'layernumber', 'shelf')

class ShelfAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id', 'shelfnumber', 'owner')

class ShelfPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('id', 'shelfnumber')
