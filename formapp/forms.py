from django import forms
from .models import application

class application_form(forms.ModelForm):
    class Meta:
       model = application
       fields = ['firstname', 'lastname', 'age', 'about']
        