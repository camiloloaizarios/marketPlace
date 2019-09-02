from django.shortcuts import render, HttpResponse
from .models import Product

def shop(request):
    products = Product.objects.all()
    return render(request,"shop.html", {'products':products})

def productDetails(request):
    return render(request,"productDetails.html")

def checkout(request):
    return render(request,"checkout.html")
