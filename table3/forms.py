from django import forms
from .models import TNA

class TnaForm(forms.ModelForm):
    class Meta:
        model = TNA
        fields = '__all__'