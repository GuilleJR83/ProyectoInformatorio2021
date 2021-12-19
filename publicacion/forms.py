# Importamos los formularios predefinidos que ya trae Django
from django import forms
from django.forms import models
from categoria.models import Categoria

from publicacion.models import Publicacion

# Definimos la clase que mostrará los campos que queremos rellenar al momento de crear una publicación
class PublicacionNuevaForm(models.ModelForm):
    titulo = forms.CharField(max_length=100, required=True, label='Título') # , help_text='Defina el título para el artículo que desea publicar.'
    contenido = forms.CharField(label='Contenido') # help_text='Escriba el texto para el artículo.'
    imagen = forms.ImageField(required=False, label='Foto', help_text='Tamaño máximo de 850 x 350 pixeles.') # , help_text='Suba una foto/imágen que aparecerá e identificará a la publicación.'
    #categoria = forms.ChoiceField(label='Categoría')
    #fechaCreacion = forms.DateTimeField(label='Fecha de creación')
    #fechaEdicion = forms.DateTimeField(label='Fecha de útlima edición')

    class Meta:
        model = Publicacion # Que tome como modelo la clase <Publicacion> que creamos

        # FIELDS permite especificar los campos a mostrar, pero a su vez, 
        # nos ahorra el trabajo de tener que espeficicar si es numerico, texto, etc., entre otras cosas
        fields = ('titulo', 'contenido', 'destacado', 'categoria') # Definimos campos a mostrar en el form de registro

# Definimos la clase que mostrará los campos que queremos rellenar al momento de crear una publicación
class PublicacionEditarForm(models.ModelForm):
    titulo = forms.CharField(max_length=100, required=True, label='Título') # , help_text='Defina el título para el artículo que desea publicar.'
    contenido = forms.CharField(label='Contenido') # help_text='Escriba el texto para el artículo.'
    imagen = forms.ImageField(required=False, label='Foto', help_text='Tamaño máximo de 850 x 350 pixeles.') # , help_text='Suba una foto/imágen que aparecerá e identificará a la publicación.'

    class Meta:
        model = Publicacion # Que tome como modelo la clase <Publicacion> que creamos

        # FIELDS permite especificar los campos a mostrar, pero a su vez, 
        # nos ahorra el trabajo de tener que espeficicar si es numerico, texto, etc., entre otras cosas
        fields = ('titulo', 'contenido', 'categoria', ) # Definimos campos a mostrar en el form de registro

class PublicacionEliminarForm(models.ModelForm):
    class Meta:
        model = Publicacion
        fields = ('titulo', )