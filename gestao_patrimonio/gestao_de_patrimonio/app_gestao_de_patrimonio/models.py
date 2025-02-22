from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Bens (models.Model):
    id  = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    setor = models.ForeignKey('Setores', null=True, on_delete=models.SET_NULL, blank=True)
    data_aquisicao = models.DateField

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
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100)
    inicio_contrato = models.DateField

    def __str__(self):
        return self.nome

class Setores (models.Model):
    id  = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome

class Movimentacao (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_movimentacao = models.DateField
    tipo_movimentacao = models.CharField(max_length=20, choices=[
        ('Entrada', 'Entrada'),
        ('Saida', 'Saida'),
        ('Transferencia', 'Transferencia')]
        )
    bem_id = models.ForeignKey('Bens', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Localizacao (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey('Setores', on_delete=models.SET_NULL, blank=True, null=True)
    bem = models.ForeignKey('Bens', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setores, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)    
def criar_perfil_usuario(instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)