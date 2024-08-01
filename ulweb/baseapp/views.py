from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.forms import UserForm
from .forms import UserInfoUpdateForm
from accounts.models import UserInfo

@login_required
def profile(request):
    if request.POST:
        form = UserInfoUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserInfoUpdateForm()
    return render(request, 'profile.html',{'form':form})


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


def contact(request):
    return render(request, 'contact.html')

def orders(request):
    return render(request, 'orders.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def user_update_form(request):
    return render(request, 'user_update_form.html')