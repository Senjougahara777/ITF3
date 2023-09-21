from django import forms 
from .models import UTP

class UtpForm(forms.ModelForm):
    class Meta:
        model = UTP 
        fields = '__all__'