from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono=models.IntegerField(max_length=15)
    
    def __str__(self):
        return self.nombre + " " + self.apellido

class Mercaderia(models.Model):
    nombre=models.CharField(max_length=50)
    codigo_barra=models.IntegerField(max_length=20)
    cantidad=models.IntegerField(max_length=300)

    def __str__(self):
        return self.nombre

class Provedor(models.Model):
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField(max_length=15)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre