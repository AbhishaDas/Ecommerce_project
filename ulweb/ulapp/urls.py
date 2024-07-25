from .import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('store/', views.store, name='store'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('product-detail/', views.product_detail, name='product-detail'),
]
