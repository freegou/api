from __future__ import unicode_literals
from django.contrib.auth.models import User
from models import UserProfile
from rest_framework import viewsets
from User.serializers import *
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from models import *
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from django.contrib.auth import login
from django.contrib import auth
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



#shop details api
class ShopDetails(APIView):
    def get(self, request, pk, format=None):
        shop = Shop.objects.get(id=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put(self, request, pk ,format=None):
        shop = Shop.objects.get(id=pk)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shop = Shop.objects.get(id=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#index api
class CompanyDetail(APIView):
    def get(self, request, format=None):
        user = UserProfile.objects.filter(user=request.user)
        serializer = CompanyDetailSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#user registeration api
class UserRegister(APIView):
    def post(self, request, format=None):
        user = User.objects.create_user(username=request.data['username'],
                                        password=request.data['password'],
                                        email=request.data['email'],
                                        first_name=request.data['first_name'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#userlist api
class UserProfileList(APIView):
    def get(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        users = UserProfile.objects.filter(company=serializer.data['company'])
        serializerd = CompanyDetailSerializer(users, many=True)
        return Response(serializerd.data, status=status.HTTP_201_CREATED)
#add user
    def post(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        p = Company.objects.get(id=serializer.data['company'])
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company=p)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#UserProfileDetail api


#Category api
class CategoryList(APIView):
    def get(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        categories = Category.objects.filter(owner=serializer.data['company'])
        serializerd = CategorySerializer(categories, many=True)
        return Response(serializerd.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        p = Company.objects.get(id=serializer.data['company'])
        serializerd = CategorySerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save(owner=p)
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)

#Category Detail api
class CategoryDetails(APIView):
    def get(self, request, pk, format=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Products api
class ProductList(APIView):
    def get(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        products = Product.objects.filter(owner=serializer.data['company'])
        serializerd = ProductSerializer(products, many=True)
        return Response(serializerd.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        p = Company.objects.get(id=serializer.data['company'])
        serializerd = AddProductSerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save(owner=p)
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)

#product details api
class ProductDeatils(APIView):
    def get(self, request, pk, format=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = Product.objects.get(id=pk)
        category = Category.objects.get(id=request.data['category'])
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Shops api
class ShopList(APIView):
    def get(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        shops = Shop.objects.filter(owner=serializer.data['company'])
        serializerd = ShopSerializer(shops, many=True)
        return Response(serializerd.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        p = Company.objects.get(id=serializer.data['company'])
        serializerd = ShopSerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save(owner=p)
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)

#Stock api
class StockList(APIView):
    def get(self, request, pk, format=None):
        #step1: use shopid find all shelfs
        shelfs = Shelf.objects.filter(owner=pk)
        serializer = ShelfSerializer(shelfs, many=True)
        #step2: use shelfs id find all units
        return Response(serializer.data)


class ShelfList(APIView):
    def post(self, request, format=None):
        serializerd = ShelfAddSerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save()
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)

class ShelfDetail(APIView):
    def get(self, request, pk, format=None):
        shelf = Layer.objects.filter(shelf=pk)
        serializer = LayerSerializer(shelf, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        shelf = Shelf.objects.get(id=pk)
        serializer = ShelfPutSerializer(shelf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shelfs = Shelf.objects.filter(id=pk)
        shelfs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LayerList(APIView):
    def post(self, request, format=None):
        serializerd = LayerAddSerializer(data=request.data)
        if serializerd.is_valid():
            serializerd.save()
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)


class Unitlist(APIView):
    def post(self, request, format=None):
        serializerd = UnitAddSerializer(data=request.data)
        product = Product.objects.get(id=request.data['product'])
        if serializerd.is_valid():
            serializerd.save(product=product)
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)

class LayerDetail(APIView):
    def delete(self, request, pk, format=None):
        layer = Layer.objects.get(id=pk)
        layer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnitDetai(APIView):
    def put(self, request, pk, format=None):
        unit = Unit.objects.get(id=pk)
        product = Product.objects.get(id=request.data['product'])
        serializerd = UnitAddSerializer(unit, data=request.data)
        if serializerd.is_valid():
            serializerd.save(product=product)
            return Response(serializerd.data, status=status.HTTP_201_CREATED)
        return Response(serializerd.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        unit = Unit.objects.get(id=pk)
        unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
