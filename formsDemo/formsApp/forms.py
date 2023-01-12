from random import choices
from select import select
from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField()
    lastName = forms.CharField()
    salary = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
#Note: single clean method validation
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if(len(inputFirstName) > 20):
            raise forms.ValidationError('The max length is 20')
"""
note:custom clean validation
    def clean_firstName(self):
        inputFirstname = self.cleaned_data['firstName']
        if(len(inputFirstname) > 20):
            raise forms.ValidationError('The max length is 20')
        return inputFirstname
"""