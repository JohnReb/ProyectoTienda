from django.db import models

# Create your models here.

class Categoria(models.Model):
    Categoria = models.CharField(max_length=30)
    FechaCreacion = models.DateField()


class Producto(models.Model):
    Producto = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=50)
    Costo = models.IntegerField()
    Disponibilidad = models.BooleanField(default=True)
    Existencias = models.SmallIntegerField()
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
