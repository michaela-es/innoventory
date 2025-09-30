from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
