from django.http import HttpResponse
from django.shortcuts import render
import math
from .models import product
def index(request):
    # products= product.objects.all()
    # n= len(products)
    # nSlides= n//4 + math.ceil((n/4)-(n//4))
    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    # params={'allProds':allProds }
    # return render(request,"ecom/index.html", params)
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:  #unique product in cats
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'ecom/index.html', params)

def about(request):
    return render(request , 'ecom/about.html')

def contact(request):
    return HttpResponse("We are at cont")
def tracker(request):
    return HttpResponse("We are at track")

def search(request):
    return HttpResponse("We are at Sera")
def productview(request):
    return HttpResponse("We are at virewt")

def checkout(request):
    return HttpResponse("We are at achecoitt")