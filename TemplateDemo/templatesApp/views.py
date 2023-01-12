from django.shortcuts import render

import templatesApp

# Create your views here.
def renderTemplate(request):
    myDict={"name":'Yaseen'}
    return render(request,'templatesApp/firstTemplate.html',context=myDict)
def renderEmployee(request):
    myDict ={'name':'Yaseen','id':'123','salary':'10000'}
    return render(request,'templatesApp/employeeDetails.html',myDict)