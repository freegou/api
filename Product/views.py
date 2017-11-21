from __future__ import unicode_literals
from rest_framework.views import APIView
from User.models import *
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from django.db.models import Sum
import json
from django.http import HttpResponse
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from User.serializers import *
from rest_framework.response import Response
import requests
from django.http import HttpResponseRedirect


@permission_classes((permissions.AllowAny,))
class Product_list(APIView):
    def get(self, request, pk, format=None):
        products = []
        for shelf in Shelf.objects.filter(owner=pk):
            for layer in Layer.objects.filter(shelf=shelf):
                for unit in Unit.objects.filter(layer=layer):
                    products.append(unit.product.id)
        products = list(set(products))
        goods = []
        for product in products:
            sku = Product.objects.get(id=product)
            units = Unit.objects.filter(product=product)
            price = units[0].price
            resp = {
                'images': sku.images,
                'name': sku.name,
                'category': sku.category.name,
                'value': sku.value,
                'description': sku.description,
                'price': price,
                'stock': Unit.objects.filter(product=product,shop=pk).aggregate(stock=Sum('number'))
            }
            goods.append(resp)
        return HttpResponse(json.dumps(goods), content_type="application/json")


@permission_classes((permissions.AllowAny,))
class Pay(APIView):
    def get(self, request, pk, pc, format=None):
        units = Unit.objects.filter(shop=pk, product=pc)
        price = units[0].price
        product = Product.objects.get(id=pc)
        data = {
            'name': product.name,
            'value': product.value,
            'category': product.category.name,
            'images': product.images,
            'code': product.code
        }
        data = json.dumps(data, ensure_ascii=False)
        order = Order(price=price, product=data, payStatus=0, payType=0)
        order.save()
        return HttpResponseRedirect('http://pay.freegou.io/s?orderId={order}&price={price}'.format(order=order.id, price=price))

@permission_classes((permissions.AllowAny,))
class Pay_Status(APIView):
    def post(self, request, format=None):
        return Response('ok')

