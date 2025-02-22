from django.shortcuts import render, redirect
from .models import Categoria
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FormInscrevase, AtualizarPerfil
# Create your views here.
@login_required
def inicio(request):
    categorias = Categoria.objects.all()
    return render(request, 'inicio.html', {'categorias': categorias})
@login_required
def categorias(request):
    return render(request, 'categorias.html')
@login_required
def fornecedores(request):
    return render(request, 'fornecedores.html')
@login_required
def bens(request):
    return render(request, 'bens.html')
@login_required
def movimentacoes(request):
    return render(request, 'movimentacoes.html')

# PARTE DE LOGIN ()usuario: funcionario_1   senha: func2025): 
@login_required
def localizacoes(request):
    return render(request, 'localizacoes.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    if request.method == 'POST':
        form = AtualizarPerfil(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AtualizarPerfil(instance=request.user)
    return render(request, 'usuario/perfil.html', {'form': form})

def inscrevase(request):
    if request.method == 'POST':
        form = FormInscrevase(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormInscrevase()
    return render(request, 'usuario/inscrevase.html', {'form': form})
