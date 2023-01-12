from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy
#from django.http import HttpResponse
#from django.views.generic import View
# Create your views here.

# class GreetingView(View):
#     def get(self,request):
#         return HttpResponse('<p>first cbvApp says Hello!!</p>')

class StudentListView(ListView):
    model = Student
    #default template_name is student_list.html
    #default context_object_name is student_list

class StudentDetailView(DetailView):
    model = Student
    #default template_name is student_detail.html
    #default context_object_name is student

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName','lastName','testScore')
    #default template_name is student_form.html
    #default context_object_name is form

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)

class StudentDeleteView(DeleteView):
    model = Student
    success_url= reverse_lazy('students')