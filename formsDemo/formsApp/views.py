from django.shortcuts import render
from . import forms

# Create your views here.
def userRegistrationView(request):
    form=forms.UserRegistrationForm()
    if request.method == 'POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print('first name:',form.cleaned_data['firstName'])
            print('last name:',form.cleaned_data['lastName'])
            print('salary:',form.cleaned_data['salary'])
            print('Gender:',form.cleaned_data['gender'])

    return render(request,'formsApp/userRegistration.html',{'form':form})