from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from Product import views

urlpatterns = [
    url(r'^shopstock/(?P<pk>[^/]+)/$', views.Product_list.as_view()),
    url(r'^pay/(?P<pk>[^/]+)/(?P<pc>[^/]+)/$', views.Pay.as_view()),
    url(r'^pay_resault/$', views.Pay_Status.as_view()),

]
