from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biografía")

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
