from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from .forms import ProductForm
from .models import Product

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


@login_required
@require_http_methods(["GET", "POST"])
def product_add_modal(request):
    form = ProductForm()
    return render(request, 'products/partials/product_modal.html', {'form': form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('HX-Request'):
                return HttpResponse('', status=204, headers={'HX-Refresh': 'true'})
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/partials/product_modal.html', {'form': form})