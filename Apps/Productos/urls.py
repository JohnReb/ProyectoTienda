from django.urls import path
from .views import categorias, ViewInfo, nuevoProducto, editarProducto, eliminarProducto, nuevoRegistroCat, editarRegistroCat, eliminarRegistroCat, ViewInfoTienda, carrito

app_name = 'Productos'
urlpatterns = [
    path('categorias', categorias, name = 'categorias'),
    path('producto', ViewInfo.as_view(), name = 'producto'),
    path('tienda', ViewInfoTienda.as_view(), name = 'tienda'),
    path('carrito', carrito, name = 'carrito'),

    path('nuevoRegistro', nuevoProducto, name="nuevoRegistro"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
    path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),


    #URLS Categorias
    path('nuevoRegistroCat', nuevoRegistroCat, name="nuevoRegistroCat"),
    path('editarRegistrocat/<idCategoria>', editarRegistroCat, name="editarRegistroCat"),
    path('eliminarRegistrocat/<idCategoria>', eliminarRegistroCat, name="eliminarRegistroCat"),
]
