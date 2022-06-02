from django.contrib import admin
from django.urls import path,include

from apps.prestar.view.usuario.view import UsuarioDelete, UsuarioUpdate, Usuariocreate, Usuarioview
from .view.prestar.view import *
from .view.libro.view import *
from .view.ejemplares.view import *
from .view.usuario.view import *
from .view.autor.view import *


app_name = 'prestar' 

urlpatterns = [ 
    path('home/',Prestarview.as_view(),name='list'),
    path('create/',Prestarcreate.as_view(),name='create'),
    path('delete/<int:pk>',PrestarDelete.as_view(),name='delete'),
    path('update/<int:pk>',PrestarUpdate.as_view(),name='update'),
    path('home/libro/',Libroview.as_view(),name='list_libro'),
    path('create/libro/',Librocreate.as_view(),name='create_libro'),
    path('delete/libro/<int:pk>',LibroDelete.as_view(),name='delete_libro'),
    path('update/libro/<int:pk>',LibrorUpdate.as_view(),name='update_libro'),
    path('home/ejemplares/',Ejemplaresview.as_view(),name='list_ejemplares'),
    path('create/ejemplares/',Ejemplarescreate.as_view(),name='create_ejemplares'),
    path('delete/ejemplares/<int:pk>',EjemplaresDelete.as_view(),name='delete_ejemplares'),
    path('update/ejemplares/<int:pk>',EjemplaresUpdate.as_view(),name='update_ejemplares'),
    path('home/usuario/',Usuarioview.as_view(),name='list_usuario'),
    path('create/usuario/',Usuariocreate.as_view(),name='create_usuario'),
    path('delete/usuario/<int:pk>',UsuarioDelete.as_view(),name='delete_usuario'),
    path('update/usuario/<int:pk>',UsuarioUpdate.as_view(),name='update_usuario'),
    path('home/autor/',Autorview.as_view(),name='list_autor'),
    path('create/autor/',Autorcreate.as_view(),name='create_autor'),
    path('delete/autor/<int:pk>',AutorDelete.as_view(),name='delete_autor'),
    path('update/autor/<int:pk>',AutorUpdate.as_view(),name='update_autor'),
]