from django import forms
from .models import Livro
from .models import Autor
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'quantidade_disponivel', 'avaliacao', 'data_de_publicacao']
    
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        empty_label="Selecione um autor",
        widget=forms.Select(attrs={'class': 'form-select'}))
    
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']