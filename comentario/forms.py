# Importamos los formularios predefinidos que ya trae Django
from django import forms
from django.forms import models, widgets

from .models import Comentario

class ComentarioNuevoForm(models.ModelForm):
    contenido = forms.CharField(max_length=100, required=True, label='Comentario')

    class Meta:
        model = Comentario
        fields = ('contenido',)

# class ComentarioEditarForm(models.ModelForm):
#     descripcion = forms.CharField(max_length=100, required=True, label='Descripción')

#     class Meta:
#         model = Categoria
#         fields = ('descripcion', )

# class CategoriaEliminarForm(models.ModelForm):
#     class Meta:
#         model = Categoria
#         fields = ('descripcion', )
