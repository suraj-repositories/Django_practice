from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):

    params = {
        'title': 'About',
        'content': 'This is the content',
        'data' : {
            "status" : True,
            "name" : "shubham",
            "age" : 23,
            "marks" : [12, 23, 43, 23, 45,43, 32],
            "html" : "<h1>This is the content</h1>",
        }
    }

    return render(request, 'about.html',params)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

# ----------------------- using model form --------------------
def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
    }
    return render(request, 'products/product_create_view.html', context)

# --------------------------- using raw form ------------------------
# def product_create_view(request, *args, **kwargs):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#
#     context = {
#         "form": form
#     }
#     return render(request, 'products/product_create_view.html', context)

def product_edit_view(request, *args, **kwargs):
    inital_data = {
        'name' : "Default name"
    }

    # ----------- To Set initial Data
    # form = ProductForm(request.POST or None, initial=inital_data)

    obj = Product.objects.get(id=1)
    # ----------- To set product form for editing...
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

    return render(request, 'products/product_create_view.html', {'form': form})

def product_details_view(request, my_id):
    product = Product.objects.get(id=my_id)
    context = {
        "product": product
    }
    return render(request, 'products/product_detail_view.html', context)

def product_view(request):
    queryset = Product.objects.all()
    return render(request, 'products/product_view.html', {'queryset': queryset})