from math import ceil

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    allProducts = []
    categories = Product.objects.values_list('category', flat=True).distinct()
    for cat in categories:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod, cat, range(1, nSlides), nSlides])

    params = {'allProducts': allProducts}
    return render(request, "shop/index.html", params)


def about(request):
    return HttpResponse("<h1>About Us</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")

def tracker(request):
    return HttpResponse("<h1>Tracking Status</h1>")

def search(request):
    return HttpResponse("<h1>Search Status</h1>")

def prodView(request):
    return HttpResponse("<h1>Product View</h1>")

def checkout(request):
    return HttpResponse("<h1>Checkout Status</h1>")