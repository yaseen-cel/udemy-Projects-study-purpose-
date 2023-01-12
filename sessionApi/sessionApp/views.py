from logging import exception
from unicodedata import name
from django.shortcuts import render
from .forms import itemForm
from django.http import HttpResponse
# Create your views here.
def pageCount(request):
    count = request.session.get('count',0)
    count = count + 1
    request.session['count'] = count
    return render(request,'sessionApp/count.html',{'count':count})

def index(request):
    request.session.set_expiry(180) #to set session timing
    raise exception('something terrible has done')
    return render(request,'sessionApp/index.html')

def addItem(request):
    form = itemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
    return render(request,'sessionApp/addItem.html',{'form':form})


def displayCart(request):
        return render(request,'sessionApp/displayItems.html')
