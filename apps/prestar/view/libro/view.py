# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ...models import *
from django.urls import reverse_lazy
from ...form import Libroforms

class Libroview(ListView):
    model = Libro
    template_name = 'libro/list.html'


class Librocreate(CreateView):
    form_class = Libroforms
    template_name = 'libro/form.html'
    model = Libro
    success_url = reverse_lazy('prestar:list_libro')

        #return super().post(request, *args, **kwargs)

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:list_libro') # esto nos dice que si fue exitoso que nos mande a esta url 

    
class LibrorUpdate(UpdateView):
    model = Libro
    template_name = 'libro/form.html'
    form_class = Libroforms
    success_url = reverse_lazy('prestar:list_libro')