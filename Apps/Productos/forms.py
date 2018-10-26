from django import forms
from.models import *;
from Apps.Productos.models import Producto;

class ProductosForm(forms.ModelForm):

  class meta:

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
      'Producto': forms.TextInput(),
      'Descripcion': forms.TextInput(),
      'Costo': forms.TextInput(),
      'Disponibilidad': forms.TextInput(),
      'Existencias': forms.TextInput(),
      'categoria': forms.TextInput(),
    }

    #attrs=({'class' : 'form-control'})