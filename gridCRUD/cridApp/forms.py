from django import forms
from cridApp.models import Employer

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'contact', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


