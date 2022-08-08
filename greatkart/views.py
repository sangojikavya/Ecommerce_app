from django.shortcuts import render
from store.models import Product
# Create your views here.

def Home(request): #function
    products=Product.objects.all().filter(is_available=True)
    return render(request,'Index.html',{'Products':products})
