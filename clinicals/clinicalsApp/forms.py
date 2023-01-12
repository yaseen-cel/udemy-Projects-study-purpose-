
from django import forms
from clinicalsApp.models import Patient,ClinicalData

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class ClinicalDataForms(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields='__all__'