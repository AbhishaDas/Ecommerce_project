from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('purchase_details/', views.purchase_details, name='purchase_details'),
    path('manage_user/<int:user_id>/', views.manage_user, name='manage_user'),
    path('products/', include('products.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


