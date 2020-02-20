from django.urls import path
from . import views



urlpatterns = [
 path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('detail/', views.detail, name='detail'),
    path('product/best/', views.best, name='best'),
]