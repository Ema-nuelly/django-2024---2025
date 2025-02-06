from django.shortcuts import render, redirect, get_object_or_404
from livros.forms import LivroForm, AutorForm

from .models import Livro, Autor
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros': livros})
@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()

    return render(request, 'cadastrar_livro.html', {'form': form})
@login_required
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()

            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    
    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})
@login_required
def informacoes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'informacoes_livro.html', {'livro': livro})
@login_required
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method in ['POST', 'GET']:
        livro.delete()
    return redirect('listar_livros')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_livros')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        return render(request, 'login.html')
    
@login_required    
def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
        else:
            print(form.errors)  
    else:
        form = AutorForm()
    return render(request, 'cadastrar_autor.html', {'form': form})


@login_required
def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})

@login_required
def deletar_autor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'deletar_autor.html', {'autor': autor})
@login_required
def autores_informacoes(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'autores_informacoes.html', {'autor': autor})

# views.py
@login_required
def cadastrar_livro_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.autor = autor
            livro.save()
            return redirect('autores_informacoes', id=autor.id)
    else:
        form = LivroForm(initial={'autor': autor.id})
    return render(request, 'cadastrar_livro.html', {
        'form': form,
        'autor': autor  
    })