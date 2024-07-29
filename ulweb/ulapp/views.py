from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserInfo


# Create your views here.
def home(request):
    return render(request, 'home.html')

def store(request):
    return render(request, 'store.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')


@login_required
def profile(request):
    if 'user_id' in request.session:
        query = request.GET.get('q')
        if query:
            user_details = UserInfo.objects.filter(
                firstname__icontains=query) | UserInfo.objects.filter(
                lastname__icontains=query) | UserInfo.objects.filter(
                email__icontains=query) | UserInfo.objects.filter(
                username__icontains=query)
        else:
            return render(request, 'profile.html', {'error':'invalid username or password'})
    else:
        return redirect('login')
        
    return render(request, 'profile.html')


def contact(request):
    return render(request, 'contact.html')

def orders(request):
    return render(request, 'orders.html')

def product_detail(request):
    return render(request, 'product-detail.html')