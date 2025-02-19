from django.contrib.auth.models import AbstractUser
from django.db import models

class TribunalParceiro(models.Model):
    sigla = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.sigla

class Usuario(AbstractUser):  # Herdando de AbstractUser para manter autenticação do Django
    tribunal = models.ForeignKey(TribunalParceiro, on_delete=models.CASCADE, default=1)
    matricula = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email_institucional = models.EmailField(unique=True)

    USERNAME_FIELD = 'email_institucional'  # Autenticação será pelo e-mail institucional
    REQUIRED_FIELDS = ['username', 'matricula', 'cpf', 'telefone']