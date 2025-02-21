from django.shortcuts import render
from .models import Categoria
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'inicio.html', {'categorias': categorias})

def categorias(request):
    return render(request, 'categorias.html')

def fornecedores(request):
    return render(request, 'fornecedores.html')

def bens(request):
    return render(request, 'bens.html')

def movimentacoes(request):
    return render(request, 'movimentacoes.html')

def localizacoes(request):
    return render(request, 'localizacoes.html')