from django.test import TestCase, Client
from livros.models import Livro, Autor
from django.urls import reverse
from django.contrib.auth.models import User

class LivroTests(TestCase):
    def test_model_creation(self):
        
        autor = Autor.objects.create(nome="Miguel de Cervantes")

        
        livro = Livro(
            titulo="Dom Quixote",
            autor=autor,  
            quantidade_disponivel=5
        )
        livro.save()

        
        self.assertEqual(livro.titulo, "Dom Quixote")
        self.assertEqual(livro.autor.nome, "Miguel de Cervantes")
        self.assertEqual(livro.quantidade_disponivel, 5)

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username='pessoa1', password='django2025')