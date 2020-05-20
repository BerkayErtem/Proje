from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

    path('base/', views.base, name='blog-base'),
    path('ChicagoPizza/', views.chicagopizza, name='blog-chicago'),
    path('NeapolitanPizza/', views.neapolitanpizza, name='blog-neapolitan'),
    path('SicilianPizza/', views.sicilianpizza, name='blog-sicilian'),
    path('TomatoPiePizza/', views.tomatopiepizza, name='blog-tomato'),


]