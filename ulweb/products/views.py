from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_dashboard(request):
    products = Product.objects.all()
    return render(request, 'product_dashboard.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_dashboard')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_dashboard')
    return render(request, 'delete_product.html', {'product': product})



