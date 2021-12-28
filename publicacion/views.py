from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from comentario.views import *
from comentario.models import *
#from cuenta.models import Usuario
from publicacion.models import *
from publicacion.forms import *

def nosotros(request):
    template = 'nosotros.html'
    contexto = {}

    return render(request, template, contexto)

def index(request): # inicio de la página web
    listado = Publicacion.objects.all().order_by('-fechaCreacion')
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

    template = 'publicacion/lista.html'
    contexto = {'publicaciones': pagina, 'page_range': page_range, }

    return render(request, template, contexto)

def autor(request, id): # devuelve los post que publicó el usuario actualmente autenticado
    listado = Publicacion.objects.filter(autor=id).order_by('-fechaCreacion')
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

    template = 'publicacion/lista.html'
    contexto = {'publicaciones': pagina, 'page_range': page_range, }

    return render(request, template, contexto)

# Mostrará el form para crear una nueva publicación
def nueva(request):
    if request.method == 'POST':
        form = PublicacionNuevaForm(request.POST, request.FILES) # Instanciamos el modelo de FORM que definimos y le asignamos el parámetro <request.POST>
                                             # para que pase los datos que ingresamos para crear el nuevo usuario.
        if form.is_valid(): # verificamos si todos los datos ingresados (principalmente los requeridos, como nombre de usuario, 
                            # email, clave) están y son válidos.
            #form.autor = Usuario.objects.get(id=request.user.id) # Usuario.objects.get(request.user)
            # Sí entra aquí, quiere decir que están bien los datos
            
            #form.save() # Asi que vamos a guardarlos (a registrar el usuario en al base de datos)
            pub = form.save(commit=False)
            pub.autor = Usuario(pk=request.user.id)
            pub.save()

            return redirect('publicacion_ver', pub.id) # retornamos una url que nos manda a cuenta/index.html (panel de opciones para el usuario)

    else: # Si el método pasado no es POST
        form = PublicacionNuevaForm() # mostramos el form vacío para que el cliente lo rellene

    contexto = {'form': form } # definimos el contexto para usar en el archivo .html
    return render(request, 'publicacion/nueva.html', contexto) # renderizamos

def editar(request, id):
    publica = Publicacion.objects.get(pk=id)
    form = PublicacionEditarForm(request.POST or None, request.FILES or None, instance=publica)
    # if not request.user == publica.autor:
    #     return redirect ('index')

    if request.method == "POST":
        if form.is_valid():
            publica = form.save()
            return redirect('publicacion_ver', id)

    contexto = {'form': form, 'publicacion': publica}
    return render (request, 'publicacion/editar.html', contexto)

def eliminar(request, id):
    publicacion = Publicacion.objects.get(pk=id)
    form = PublicacionEliminarForm(request.POST or None, instance=publicacion)

    if request.method == 'POST':
        publicacion.delete()
        return redirect('index')

    template = 'publicacion/eliminar.html'
    contexto = {'form': form, 'publicacion': publicacion}
    return render (request, template, contexto)

def ver(request, id):
    publica = Publicacion.objects.get(pk=id)
    form = ComentarioNuevoForm(request.POST or None)
    likes = Like.objects.filter(usuario=request.user).all().count()

    if request.method == "POST":
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor=Usuario(pk=request.user.id)
            comentario.publicacion=publica
            comentario.save()
            return redirect('comentario_ver', id, comentario.id)
        print(form.errors)
    
    comentarios = Comentario.objects.filter(publicacion=id).order_by('-fechaComentario') # publica.getComentarios()
    contexto = {'publicacion': publica, 'comentarios': comentarios, 'form': form}

    return render(request, 'publicacion/publicacion.html', contexto)
