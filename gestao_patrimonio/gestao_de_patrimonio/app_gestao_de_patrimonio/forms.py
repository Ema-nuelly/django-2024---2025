from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormInscrevase(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class AtualizarPerfil(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")