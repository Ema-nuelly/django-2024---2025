from django.db import models
from django.core.exceptions import ValidationError
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emma_biblioteca.settings')

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    def quantidade_livros(self):
        return self.livro_set.count()
    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros') 
    quantidade_disponivel = models.IntegerField(null=True, blank=True)
    avaliacao = models.FloatField(null=True, blank=True) 
    data_de_publicacao = models.DateField(null=True, blank=True)


# --- CRIAÇÃO DA TABELA VIA DJANGO
# class Livro(models.Model):
#     titulo = models.CharField(max_length=100)
#     quantidade_disponivel = models.IntegerField()
#     avaliacao = models.FloatField(null=True, blank=True)
#     data_de_publicacao = models.DateField(null=True, blank=True)

# --- INSERÇÃO DE DADOS
# INSERT INTO livros_livro (titulo, quantidade_disponivel, avaliacao, data_de_publicacao) VALUES
# ("O Cortiço", 5, 3.2, "1890-01-01"),
# ("Dom Casmurro", 3, 4.5, "1900-01-01"),
# ("Memórias Póstumas de Brás Cubas", 7, 4.7, "1881-01-01"),
# ("Senhora", 2, 3.8, "1875-01-01"),
# ("Grande Sertão: Veredas", 4, 4.9, "1956-01-01"),
# ("A Moreninha", 8, 4.0, "1844-01-01"),
# ("Iracema", 6, 4.3, "1865-01-01"),
# ("O Primo Basílio", 3, 4.1, "1878-01-01"),
# ("Cem Anos de Solidão", 9, 4.8, "1967-01-01"),
# ("Shrek: The Untold Swamp Saga", 20, 5.0, "2001-05-18");

# --- NO PROCESSO, CRIEI ROWS DUPLICADAS, ENTÃO...
# DELETE FROM livros_livro 
# WHERE id = 1;

# --- NÃO PERCEBI QUE SÃO CINCO ATRIBUTOS, ENTÃO...
# ALTER TABLE livros_livro
# ADD COLUMN autor VARCHAR(100);

# --- COLOCANDO DADOS NESSA NOVA COLUNA:
# UPDATE livros_livro
# SET autor = 'Aluísio Azevedo'
# WHERE titulo = 'O Cortiço';

# UPDATE livros_livro
# SET autor = 'Machado de Assis'
# WHERE titulo = 'Dom Casmurro';

# UPDATE livros_livro
# SET autor = 'Joaquim Maria Machado de Assis'
# WHERE titulo = 'Memórias Póstumas de Brás Cubas';

# UPDATE livros_livro
# SET autor = 'José de Alencar'
# WHERE titulo = 'Senhora';

# UPDATE livros_livro
# SET autor = 'João Guimarães Rosa'
# WHERE titulo = 'Grande Sertão: Veredas';

# UPDATE livros_livro
# SET autor = 'Joaquim Manuel de Macedo'
# WHERE titulo = 'A Moreninha';

# UPDATE livros_livro
# SET autor = 'José de Alencar'
# WHERE titulo = 'Iracema';

# UPDATE livros_livro
# SET autor = 'José de Alencar'
# WHERE titulo = 'O Primo Basílio';

# UPDATE livros_livro
# SET autor = 'Gabriel García Márquez'
# WHERE titulo = 'Cem Anos de Solidão';

# UPDATE livros_livro
# SET autor = 'Fiona the Ogre'
# WHERE titulo = 'Shrek: The Untold Swamp Saga';

# --- SELECIONANDO TODOS OS CAMPOS:
# SELECT * FROM livros_livro 

# --- SELECIONANDO SOMENTE TITULO, AUTOR E DISPONIBILIDADE
# SELECT titulo, autor, quantidade_disponivel FROM livros_livro 

# --- SELECIONANDO LIVROS DISPONÍVEIS EM MAIOR QUANTIDADE
# SELECT titulo, autor, quantidade_disponivel FROM livros_livro WHERE quantidade_disponivel > 5

# --- ATUALIZANDO A QUANTIDADE DISPONÍVEL DE UM LIVRO
# UPDATE livros_livro
# SET quantidade_disponivel = 5
# WHERE titulo = 'Dom Casmurro';

# --- SELECIONANDO LIVROS ORDENDOS POR QUANTIDADE DISPONÍVEL
# SELECT titulo, autor, quantidade_disponivel 
# FROM livros_livro 
# ORDER BY quantidade_disponivel DESC;

# --- CONTANDO O NÚMERO DE LIVROS DISPONÍVEIS
# SELECT COUNT(*) 
# FROM livros_livro 
# WHERE quantidade_disponivel > 0;
