from django.db.models import Prefetch
from django.shortcuts import render
from category.models import Category
from product.models import Product, ProductImage
from .forms import EmailForm
from django.core.mail import send_mail




def main(request):
    categories = Category.objects.filter(is_main=True)
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images')).order_by('-created_at')[:6]
    print(products)
    ctx = {
        "categories": categories,
        "products": products,
        "a" : 1234567890
    }
    return render(request, 'index.html', ctx)


def contact(request):
    form = EmailForm()
    print("START...")
    send_mail(
        'Subject here',
        'Here is the message.',
        'nurullostepn3@gmail.com',
        ['obidzeromax@gmail.com'],
        fail_silently=False,
    )
    print('END.....')
    ctx = {
        "form": form
    }
    return render(request, 'contact.html', ctx)