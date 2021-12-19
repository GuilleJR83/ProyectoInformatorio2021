# Importamos los formularios predefinidos que ya trae Django
from django import forms
from django.forms import models

from .models import Categoria

class CategoriaNuevaForm(models.ModelForm):
    descripcion = forms.CharField(max_length=100, required=True, label='Descripción')

    class Meta:
        model = Categoria
        fields = ('descripcion', )

class CategoriaEditarForm(models.ModelForm):
    descripcion = forms.CharField(max_length=100, required=True, label='Descripción')

    class Meta:
        model = Categoria
        fields = ('descripcion', )

class CategoriaEliminarForm(models.ModelForm):
    class Meta:
        model = Categoria
        fields = ('descripcion', )
