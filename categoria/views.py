from django.shortcuts import render, HttpResponse, redirect

from .models import Categoria
from publicacion.models import Publicacion
from .forms import *
#from publicacion.forms import *

def listado(request):
    template = 'categoria/lista.html'
    contexto = {} # ya lo tenemos entre los procesadores de contexto

    return render(request, template, contexto)

def nueva(request):
    if request.method == 'POST':
        form = CategoriaNuevaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_listado')

    else:
        form = CategoriaNuevaForm()

    contexto = {'form': form, }
    return render(request, 'categoria/nueva.html', contexto)

def editar(request, id):
    categoria = Categoria.objects.get(pk=id)
    form = CategoriaEditarForm(request.POST or None, instance=categoria)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('categoria_listado') # debe retornar al mismo lugar en el que estaba

    template = 'categoria/editar.html'
    contexto = {"form": form}
    return render (request, template, contexto)

def eliminar(request, id):
    categoria = Categoria.objects.get(pk=id)
    form = CategoriaEliminarForm(request.POST or None, instance=categoria)

    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_listado') # debe retornar al mismo lugar en el que estaba

    template = 'categoria/eliminar.html'
    contexto = {'form': form, 'categoria': categoria}
    return render (request, template, contexto)

def filtrar(request, id):
    listado = Publicacion.objects.filter(categoria_id=id)

    template = 'categoria/filtrar.html'
    contexto = {'publicaciones': listado}
    return render(request, template, contexto)
