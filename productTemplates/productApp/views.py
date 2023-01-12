from django.shortcuts import render

# Create your views here.
def electronics(request):
    productDict={
         'product1':'Mac',
         'product2':'IPhone',
         'product3':'Dell',

    }
    return render(request,'productApp/product.html',productDict)
def toys(request):
    productDict={
         'product1':'Remote Car',
         'product2':'Drone',
         'product3':'Rocket',

    }
    return render(request,'productApp/product.html',productDict)
def shoes(request):
    productDict={
         'product1':'Nike',
         'product2':'Puma',
         'product3':'Adidas',

    }
    return render(request,'productApp/product.html',productDict)
def index(request):
    return render(request,'productApp/index.html')