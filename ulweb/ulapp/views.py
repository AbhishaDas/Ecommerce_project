from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def store(request):
    return render(request, 'store.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def cart(request):
    return render(request, 'cart.html')

def profile(request):
    return render(request, 'profile.html')

def product_detail(request):
    return render(request, 'product-detail.html')