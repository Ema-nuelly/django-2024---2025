from django.shortcuts import render, redirect
from .models import Categoria, PerfilUsuario
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FormInscrevase, AtualizarPerfil, SetorF
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
    user_profile, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        perfil_form = AtualizarPerfil(request.POST, instance=request.user)
        setor_form = SetorF(request.POST, instance=user_profile)

        if perfil_form.is_valid() and setor_form.is_valid():
            perfil_form.save()
            setor_form.save()
            return redirect('perfil')
    else:
        perfil_form = AtualizarPerfil(instance=request.user)
        setor_form = SetorF(instance=user_profile)

    return render(request, 'usuario/perfil.html', {'perfil_form': perfil_form, 'setor_form': setor_form})
def inscrevase(request):
    if request.method == 'POST':
        form = FormInscrevase(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormInscrevase()
    return render(request, 'usuario/inscrevase.html', {'form': form})
