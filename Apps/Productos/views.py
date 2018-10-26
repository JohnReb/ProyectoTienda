from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import  ListView
from Apps.Productos.models import Producto, Categoria
from Apps.Productos.forms import ProductosForm

# Create your views here.

def index(request):
    return HttpResponse("Esta es la Respuesta")

def producto(request):
    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, 'productos/index.html', contexto)

def categorias(request):
    contexto = {
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categorias/index.html', contexto)
    #'clientes/pagina.html', contexto)

class ViewInfo(ListView):
    model = Producto
    #template_name = 'productos/index.html'
    queryset = Producto.objects.all()
    template_name = 'productos/index.html'


def nuevoProducto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Productos:productos')
    else:
        form = ProductosForm()
    return render(request, 'productos/productoFormulario.html', {'form': form})


def editarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    if request.method == 'GET':
        form = ProductosForm(instance=producto)
    else:
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos.listarClientes')
    return render(request, 'productos/productoFormulario.html', {'form': form})

def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)

