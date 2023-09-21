from django import forms 
from .models import DTPA

class DtpaForm(forms.ModelForm):
    class Meta:
        model = DTPA 
        fields = '__all__'