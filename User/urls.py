from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from User import views

urlpatterns = [
    url(r'^register', views.UserRegister.as_view()),
    url(r'^index', views.CompanyDetail.as_view()),
    url(r'^users', views.UserProfileList.as_view()),
    url(r'^categories', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[^/]+)/$', views.CategoryDetails.as_view()),
    url(r'^products', views.ProductList.as_view()),
    url(r'^shops/$', views.ShopList.as_view()),
    url(r'^shop/(?P<pk>[^/]+)/$', views.ShopDetails.as_view()),
    url(r'^product/(?P<pk>[^/]+)/$', views.ProductDeatils.as_view()),
    url(r'^stock/(?P<pk>[^/]+)/$', views.StockList.as_view()),
    url(r'^units/$', views.Unitlist.as_view()),
    url(r'^unit/(?P<pk>[^/]+)/$', views.UnitDetai.as_view()),
    url(r'^layers/$', views.LayerList.as_view()),
    url(r'^shelf/(?P<pk>[^/]+)/$', views.ShelfDetail.as_view()),
    url(r'^shelfs/$', views.ShelfList.as_view()),
    url(r'^layer/(?P<pk>[^/]+)/$', views.LayerDetail.as_view()),
]
