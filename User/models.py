from __future__ import unicode_literals
import uuid
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    card = models.CharField(max_length=80)
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company)
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shopid = models.CharField(max_length=30)
    remarker = models.CharField(max_length=30)
    gps = models.CharField(max_length=50, unique=True)
    isonline = models.IntegerField(default=1)
    owner = models.ForeignKey(Company)
    createtime = models.DateTimeField(default=timezone.now, editable=False)
    updatetime = models.DateTimeField(auto_now=True)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Company)
    name = models.CharField(max_length=20, unique=True, )
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Company)
    category = models.ForeignKey(Category )
    name = models.CharField(max_length=40)
    value = models.CharField(max_length=20)
    code = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    search = models.CharField(max_length=300)
    images = models.URLField()
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class Shelf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shelfnumber = models.IntegerField(default=0)
    owner = models.ForeignKey(Shop, related_name='shelfs',  null=True, on_delete=models.SET_NULL)
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class Layer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    layernumber = models.IntegerField(default=0)
    shelf = models.ForeignKey(Shelf, related_name='shelf_layers', null=True, on_delete=models.SET_NULL)
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(Shop)
    offset = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    price = models.CharField(max_length=30)
    product = models.ForeignKey(Product,related_name='products', null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    layer = models.ForeignKey(Layer, related_name='shelf_units', null=True, on_delete=models.SET_NULL)
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)
    updatetime = models.DateTimeField('update time', auto_now=True)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.CharField(max_length=20)
    payType = models.IntegerField()
    payStatus  = models.IntegerField() #default = 0
    product = models.TextField(max_length=999)
    openId = models.CharField(max_length=80) #add shopid
    createtime = models.DateTimeField('create time', default=timezone.now, editable=False)


