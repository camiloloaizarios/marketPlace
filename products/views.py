from django.shortcuts import render, HttpResponse

def shop(request):
    return render(request,"shop.html")

def productDetails(request):
    return render(request,"productDetails.html")

def checkout(request):
    return render(request,"checkout.html")
