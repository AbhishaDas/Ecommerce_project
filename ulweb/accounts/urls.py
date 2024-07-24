from .import views
from django.urls import path

urlpatterns = [   
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('product_dashboard/', views.product_dashboard, name='product_dashboard'),
    path('purchase_details/', views.purchase_details, name='purchase_details'),
    path('manage_user/<int:user_id>/', views.manage_user, name='manage_user'),
]


