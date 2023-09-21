from django import forms 
from .models import STP2

class Stp2Form(forms.ModelForm):
    class Meta:
        model = STP2 
        fields = '__all__'