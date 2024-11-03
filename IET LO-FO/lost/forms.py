from django import forms
from .models import kunal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class kunalform(forms.ModelForm):
    
    class Meta:
        model = kunal
        fields =['text','photo']

class registrationform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields =('username','email','password1','password2')