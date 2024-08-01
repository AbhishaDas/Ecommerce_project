from .import views
from django.urls import path, include

urlpatterns = [
    path('',views.home, name='home'),
    path('store/', views.store, name='store'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('orders/', views.orders, name='orders'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('user_update_form/',views.user_update_form, name='user_update_form'),
    path('accounts/', include('accounts.urls'))
]