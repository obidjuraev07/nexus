from django.shortcuts import render, redirect
from django.db.models import Prefetch
from django.core.paginator import Paginator
from .models import Product, ProductImage
from .forms import ProductForm


def product_list(request):
    page = request.GET.get('page', 1)
    print('PAGE', page)
    products = Product.objects.prefetch_related(Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(page)
    ctx = {
        "products": products,
        "page_obj": page_obj,
        'count': paginator.count
    }
    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    ctx = {

    }
    return render(request, 'detail.html', ctx)

def product_add(request):

    if request.method == "POST":
        form = ProductForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            product = form.save(commit=False)
            print('USER', request.user.profile)
            product.user = request.user.profile
            product.save()
            return redirect('main')
    else:
        form = ProductForm()
    ctx = {
        "form": form
    }

    return render(request, 'product_add.html', ctx)