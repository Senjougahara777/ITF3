from django import forms 
from .models import NDTP

class NdtpForm(forms.ModelForm):
    class Meta:
        model = NDTP
        fields = '__all__'