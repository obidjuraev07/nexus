from django.shortcuts import render
from .models import Product
def product_list(request):

    ctx = {

    }
    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {

    }
    return render(request, 'detail.html', ctx)