from django.urls import path
from .views import index, producto, categorias, ViewInfo, nuevoProducto, editarProducto, eliminarProducto

app_name = 'Productos'
urlpatterns = [
    path('index', index),
    path('', index),
    #path('productos', producto),
    path('categorias', categorias),
    path('productos', ViewInfo.as_view()),

    path('nuevoRegistro', nuevoProducto, name="nuevoRegistro"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
    path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),
]
