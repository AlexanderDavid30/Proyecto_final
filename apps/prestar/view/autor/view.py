# Create your views here.
from re import A
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ...models import *
from django.urls import reverse_lazy
from ...form import Autorforms

class Autorview(ListView):
    model = Autor
    template_name = 'autor/list.html'


class Autorcreate(CreateView):
    form_class = Autorforms
    template_name = 'autor/form.html'
    model = Autor
    success_url = reverse_lazy('prestar:list_autor')

        #return super().post(request, *args, **kwargs)

class AutorDelete(DeleteView):
    model = Autor
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:list_autor') # esto nos dice que si fue exitoso que nos mande a esta url 

    
class AutorUpdate(UpdateView):
    model = Autor
    template_name = 'autor/form.html'
    form_class = Autorforms
    success_url = reverse_lazy('prestar:list_autor')