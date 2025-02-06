from django.urls import path
from livros.views import listar_livros, cadastrar_livro, editar_livro, informacoes_livro, excluir_livro, custom_login, custom_logout, add_autor, listar_autores, deletar_autor, autores_informacoes, cadastrar_livro_autor

urlpatterns = [
    path('livros', listar_livros, name='listar_livros'),
    path('cadastrar_livro/', cadastrar_livro, name='cadastrar_livro'),
    path('editar_livro/<int:pk>/', editar_livro, name='editar_livro'),
    path('informacoes_livro/<int:pk>/', informacoes_livro, name='informacoes_livro'),
    path('excluir_livro/<int:pk>/', excluir_livro, name='excluir_livro'),
    path('', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('novo-autor/', add_autor, name='novo_autor'),
    path('listar-autores/', listar_autores, name='listar_autores'),
    path('autor/delete/<int:id>/', deletar_autor, name='deletar_autor'),
    path('autor/informacoes/<int:id>/', autores_informacoes, name='autores_informacoes'),
    path('autor/<int:autor_id>/add-livro/', cadastrar_livro_autor, name='cadastrar_livro_autor'),
]
