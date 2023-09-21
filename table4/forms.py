from django import forms
from .models import TTPD

class TtpdForm(forms.ModelForm):
    class Meta:
        model = TTPD
        fields = '__all__'