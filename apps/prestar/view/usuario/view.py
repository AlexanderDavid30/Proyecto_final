# Create your views here.
from re import A
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ...models import *
from django.urls import reverse_lazy
from ...form import Usuarioforms

class Usuarioview(ListView):
    model = Usuario
    template_name = 'usuario/list.html'


class Usuariocreate(CreateView):
    form_class = Usuarioforms
    template_name = 'usuario/form.html'
    model = Usuario
    success_url = reverse_lazy('prestar:list_usuario')

        #return super().post(request, *args, **kwargs)

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:list_usuario') # esto nos dice que si fue exitoso que nos mande a esta url 

    
class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = 'usuario/form.html'
    form_class = Usuarioforms
    success_url = reverse_lazy('prestar:list_usuario')