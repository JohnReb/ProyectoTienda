from django import forms
from  Apps.Productos.models import Producto, Categoria

class ProductosForm(forms.ModelForm):
  class Meta:
    model = Producto
    fields = [
      'Producto',
      'Descripcion',
      'Costo',
      'Disponibilidad',
      'Existencias',
      'categoria',
    ]
    labels = {
      'Producto' : 'Nombre del producto',
      'Descripcion' : 'Descripcion del producto',
      'Costo' : 'Costo del producto',
      'Disponibilidad' : 'Disponibilidad',
      'Existencias' : 'Existencias',
      'categoria' : 'Nombre de categoria',
    }
    widgets = {
      'Producto': forms.TextInput(attrs={'class': 'form-control'}),
      'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'Costo': forms.TextInput(attrs={'class': 'form-control'}),
      'Disponibilidad': forms.TextInput(attrs={'class': 'form-control'}),
      'Existencias': forms.TextInput(attrs={'class': 'form-control'}),
      'categoria': forms.TextInput(attrs={'class': 'form-control'}),
    }

#Form Categorias
class CategoriasForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = [
      'Categoria',
      'FechaCreacion'
    ]
    labels = {
      'Categoria': 'Nombre',
      'FechaCreacion': 'Fecha de Creacion',
    }
    widgets = {
      'Categoria': forms.TextInput(attrs={'class': 'form-control'}),
      'FechaCreacion': forms.TextInput(attrs={'class':'form-comtrol'}),
    }