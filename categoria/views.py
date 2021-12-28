from django.shortcuts import render, redirect
from django.core.paginator import Paginator

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
    listado = Publicacion.objects.filter(categoria_id=id).order_by('-fechaCreacion')
    paginador = Paginator(listado, 3) # cuatro post por página
    
    nPagina = request.GET.get('pg')
    pagina = paginador.get_page(nPagina)

    # Fuente: https://www.it-swarm-es.com/es/django/mostrar-solo-algunos-de-los-numeros-de-pagina-por-paginacion-django/1052946339/

    # Get the index of the current page
    index = pagina.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginador.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns 
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginador.page_range)[start_index:end_index]

    template = 'categoria/filtrar.html'
    contexto = {'publicaciones': pagina, 'page_range': page_range, }

    return render(request, template, contexto)
