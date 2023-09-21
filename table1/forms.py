from django import forms
from .models import BasicForm

class FormBasicForm(forms.ModelForm):
    class Meta:
        model = BasicForm
        fields = '__all__'