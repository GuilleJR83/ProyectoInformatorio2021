# Importamos RENDER y REDIRECT
from django.shortcuts import render, redirect

from cuenta.models import Usuario
from publicacion.models import Publicacion

from .models import Comentario
from .forms import *

def nuevo(request, publicacion_id):
    if request.method == 'POST':
        form = ComentarioNuevoForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = Publicacion(pk=publicacion_id)
            comentario.autor = Usuario(pk=request.user.id)
            comentario.save()

            return redirect('comentario_ver', publicacion_id, comentario.id)

    else:
        form = ComentarioNuevoForm()

    contexto = {'form': form, } # definimos el contexto para usar en el archivo .html
    return render(request, 'comentario/nuevo.html', contexto) # renderizamos

# def editar(request, id):
#     publica = Publicacion.objects.get(pk=id)
#     form = PublicacionEditarForm(request.POST or None, instance=publica) 
#     #Al entrar a editar, no quiero que me aparezca los datos vacios
#     print("metodo:",request.method)
#     if request.method == "POST":
#         if form.is_valid():
#             publica = form.save()
#             return redirect('index')

#     contexto = {"form":form}
#     return render (request,'publicacion/editar.html', contexto)

# def eliminar(request, id):
#     publicacion = Publicacion.objects.get(pk=id)
#     form = PublicacionEliminarForm(request.POST or None, instance=publicacion)

#     if request.method == 'POST':
#         publicacion.delete()
#         return redirect('index')

#     template = 'publicacion/eliminar.html'
#     contexto = {'form': form, 'publicacion': publicacion}
#     return render (request, template, contexto)

def ver(request, publicacion_id, comentario_id):
    # publicacion = Publicacion.objects.get(pk=publicacion_id)
    # comentario = Comentario.objects.get(pk=comentario_id)
    # contexto = {"Publicacion": publicacion}
    # return render(request, 'comentario/comentario.html', contexto)
    #return redirect('comentario_ver', publicacion_id, comentario_id)
    return redirect('publicacion_ver', publicacion_id)
