from django.contrib import admin
from Apps.Productos.models import Producto, Categoria

# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
