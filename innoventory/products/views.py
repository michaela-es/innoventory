from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import ProductForm
from .models import Product


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


@login_required
def product_modal(request):
    form = ProductForm()
    return render(request, 'products/partials/product_modal.html', {'form': form})


@login_required
@require_POST
def add_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('', status=204, headers={'HX-Refresh': 'true'})
    else:
        return render(request, 'products/partials/product_modal.html', {'form': form})