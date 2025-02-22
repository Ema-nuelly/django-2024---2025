from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario, Setores

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

class SetorF(forms.ModelForm):
    setor = forms.ModelChoiceField(queryset=Setores.objects.all(), required=True, label="Selecione seu setor:") 

    class Meta:
        model = PerfilUsuario
        fields = ['setor']