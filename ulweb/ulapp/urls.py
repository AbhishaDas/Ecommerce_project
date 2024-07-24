from .import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('product-detail/', views.product_detail, name='product-detail'),
]
