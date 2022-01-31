from math import ceil
from django.shortcuts import render
from .models import Product


# Create your views here.


def index(request):
    allprods = []
    cateprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cateprods}
    for cat in cats:
        product = Product.objects.filter(category=cat)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([product, range(1, nSlides), nSlides])
    params = {'all_prods': allprods}
    return render(request, 'shop/index.html', params)


def About(request):
    return render(request, 'shop/about.html')

def tracker(request):
    return render(request, 'shop/tracker.html')


def products(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/product.html', {'product': product})


def contact(request):
    return render(request, 'shop/contact.html')