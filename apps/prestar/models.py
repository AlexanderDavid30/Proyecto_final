from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ejemplaresid = models.ManyToManyField('Ejemplares', related_name='ejemplaresid', through='Prestar')

    def __str__(self) -> str:
        return self.nombre

class Ejemplares(models.Model):
    localizacion = models.CharField(max_length=50)
    usuarioid = models.ManyToManyField('Usuario', related_name='usuarioid', through='Prestar')
    libro = models.ManyToManyField('Libro', related_name='libro')

    def __str__(self) -> str:
        return self.localizacion
    

class Prestar(models.Model):
    fecha_dev = models.DateField(default=timezone.now)
    fecha_prest = models.DateField(default=timezone.now)
    usuarioid = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    ejemplaresid = models.ForeignKey(Ejemplares,on_delete=models.CASCADE)

class Autor(models.Model):
    nombre = models.CharField(max_length=50)

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    num_pag = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    autorid = models.ManyToManyField(Autor, related_name='autorid')