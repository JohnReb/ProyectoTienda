from django.db import models

# Create your models here.

class Categoria(models.Model):
    Categoria = models.CharField(max_length=30)
    FechaCreacion = models.DateField()

    def NombreCategoria(self):
        cadena = "{0}"
        return cadena.format(self.Categoria)

    def __str__(self):
        return self.NombreCategoria()


class Producto(models.Model):
    Producto = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=50)
    Costo = models.IntegerField()
    Disponibilidad = models.BooleanField(default=True)
    Existencias = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def NombreProducto(self):
        cadena = "{0}"
        return cadena.format(self.Producto)

    def __str__(self):
        return self.NombreProducto()


class Ticket(models.Model):
    Producto = models.CharField(max_length=30)
    Costo = models.IntegerField()
    Cantidad = models.IntegerField()