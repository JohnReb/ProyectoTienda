from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from Apps.Productos.models import Producto, Categoria
from Apps.Productos.forms import ProductosForm, CategoriasForm

# Create your views here.


def index(request):
    return HttpResponse("Esta es la Respuesta")


def producto(request):
    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, 'productos/listaProductos.html', contexto)


def categorias(request):
    contexto = {
        'categorias': Categoria.objects.all()
    }
    return render(request, 'categorias/index.html', contexto)


class ViewInfoTienda(ListView):
    model = Producto
    template_name = 'carrito/carrito.html'


def carrito(request):
    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, 'carrito/ticket.html', contexto)

def pagar(request):
    datos = request.GET.get("productos")
    datos = json.loads(datos)
    # print datos
    for prod in datos:
        producto = Producto.objects.filter(pk=prod[0]).first()
        cantidad = producto.Existencias
        nueva_Existencia = int(cantidad)- int(datos[prod[0]]["cantidad"])
        if nueva_Existencia < 0:
            estatus = "No hay suficientes productos"
        else:
            producto.Existencias = nueva_Existencia
            producto.save()
            estatus="OK"
    return HttpResponse(estatus)


class ViewInfo(ListView):
    model = Producto
    template_name = 'productos/listaProductos.html'

def nuevoProducto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Productos:producto')
    else:
        contexto = {
            'categorias': Categoria.objects.all(),
            'form': ProductosForm()
        }
    return render(request, 'productos/productoFormulario.html', contexto)


def editarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    if (request.method == 'GET'):
        form = ProductosForm(instance=producto)
    else:
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos.producto')
    return render(request, 'productos/productoFormulario.html', {'form': form})

def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    producto.delete()
    return redirect('Productos:producto')


## -- Views Categorias
##

def nuevoRegistroCat(request):
    if request.method == 'POST':
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Productos:categorias');
    else:
        form = CategoriasForm()
    return render(request, 'categorias/categoriasFormulario.html', {'form': form})


def editarRegistroCat(request, idCategoria):
    categoria = Categoria.objects.get(id=idCategoria)
    if (request.method == 'GET'):
        form = CategoriasForm(instance=categoria)
    else:
        form = CategoriasForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save();
        return redirect('Productos:categorias')
    return render(request, 'categorias/categoriasFormulario.html', {'form': form})


def eliminarRegistroCat(request, idCategoria):
    categoria = Categoria.objects.get(id=idCategoria)
    categoria.delete()
    return redirect('Productos:categorias')
