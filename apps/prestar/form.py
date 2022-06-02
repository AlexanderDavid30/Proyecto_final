from django.forms.models import ModelForm
from .models import Autor, Ejemplares, Libro, Prestar, Usuario


class Prestarforms(ModelForm):
    class Meta:
        model = Prestar
        fields = '__all__'

class Libroforms(ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class Ejemplaresforms(ModelForm):
    class Meta:
        model = Ejemplares
        fields = '__all__'

class Usuarioforms(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class Autorforms(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'