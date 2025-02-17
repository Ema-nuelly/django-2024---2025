from django.db import models

# Create your models here.
class Bens (models.Model):
    id  = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    categoria_id = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    fornecedor_id = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    data_aquisicao = models.DateField(max_length=100)

    def __str__(self):
        return self.nome

class Categoria (models.Model):
    id  = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Fornecedor (models.Model):
    id  = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    inicio_contrato = models.DateField(max_length=100)

    def __str__(self):
        return self.nome


