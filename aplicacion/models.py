from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.IntegerField()

class Top(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()

class Camisas(models.Model):
    marca = models.CharField(max_length=50)
    talle= models.IntegerField()    

