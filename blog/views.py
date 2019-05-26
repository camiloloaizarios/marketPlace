from django.shortcuts import render, HttpResponse

def blog(request):
    return render(request,"blog.html")

def blogDetails(request):
    return render(request,"blogDetails.html")

