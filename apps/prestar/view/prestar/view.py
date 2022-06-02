# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ...models import *
from django.urls import reverse_lazy
from ...form import Prestarforms
from django.http import HttpResponseRedirect

class Prestarview(ListView):
    model = Prestar
    template_name = 'prestar/list.html'


class Prestarcreate(CreateView):
    form_class = Prestarforms
    template_name = 'prestar/form.html'
    model = Prestar
    success_url = reverse_lazy('prestar:list')

        #return super().post(request, *args, **kwargs)

class PrestarDelete(DeleteView):
    model = Prestar
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:list') # esto nos dice que si fue exitoso que nos mande a esta url 

    
class PrestarUpdate(UpdateView):
    model = Prestar
    template_name = 'prestar/form.html'
    form_class = Prestarforms
    success_url = reverse_lazy('prestar:list')