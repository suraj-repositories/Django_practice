from django.http import HttpResponse
from django.shortcuts import render

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
