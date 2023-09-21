from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['name','avatar','username','email','password1','password2','is_AreaManager','is_HOT','is_CDN','is_verified']

    
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]