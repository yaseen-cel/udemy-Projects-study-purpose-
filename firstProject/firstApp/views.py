from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse('<h1>My first Django App</h1>')

def displaytime(request):
    dt=datetime.datetime.now()
    s='<b>Current date and time is : </b>'+str(dt)
    return HttpResponse(s)
