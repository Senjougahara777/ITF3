from django import forms 
from .models import STP

class StpForm(forms.ModelForm):
    class Meta:
        model = STP 
        fields = '__all__'