# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ...models import *
from django.urls import reverse_lazy
from ...form import Ejemplaresforms

class Ejemplaresview(ListView):
    model = Ejemplares
    template_name = 'ejemplares/list.html'


class Ejemplarescreate(CreateView):
    form_class = Ejemplaresforms
    template_name = 'ejemplares/form.html'
    model = Ejemplares
    success_url = reverse_lazy('prestar:list_ejemplares')

        #return super().post(request, *args, **kwargs)

class EjemplaresDelete(DeleteView):
    model = Ejemplares
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:list_ejemplares') # esto nos dice que si fue exitoso que nos mande a esta url 

    
class EjemplaresUpdate(UpdateView):
    model = Ejemplares
    template_name = 'ejemplares/form.html'
    form_class = Ejemplaresforms
    success_url = reverse_lazy('prestar:list_ejemplares')