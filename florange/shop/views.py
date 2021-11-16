from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    params = {'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    # return HttpResponse("We are at about")
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact")
    # return render(request, 'shop/contact.html')


def search(request):
    return HttpResponse("We are at search")
    # return render(request, 'shop/search.html')


def productview(request):
    return HttpResponse("We are at product view")
    # return render(request, 'shop/productview.html')


def tracker(request):
    return HttpResponse("We are at tracker")
    # return render(request, 'shop/tracker.html')
