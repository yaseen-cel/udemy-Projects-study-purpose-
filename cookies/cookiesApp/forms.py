
from django import forms

class itemForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()