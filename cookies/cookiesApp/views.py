from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .forms import itemForm
# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse('<h2>Home Page</h2>')
def page2(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled!!')
    request.session.delete_test_cookie()
    return HttpResponse('<b>Page 2</b>')

#to see howmany times opened the page
def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count']) + 1
    else:
        count=1
    response = render(request,'cookiesApp/count.html',{'count':count})
    response.set_cookie('count',count)
    return response

def index(request):
    return render(request,'cookiesApp/index.html')

def addItem(request):
    form = itemForm()
    response = render(request,'cookiesApp/addItem.html',{'form':form})
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity,120)
    return response

def displayCart(request):
        return render(request,'cookiesApp/displayItems.html')
