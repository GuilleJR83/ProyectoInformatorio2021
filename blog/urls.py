#from django.conf import settings
from django.conf.urls.static import static
from django import views
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.utils import decorators
from blog import settings #from .settings import local

import categoria.views, comentario.views, cuenta.views, publicacion.views

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls), # sitio de administración

    path('', publicacion.views.index, name='index'), # inicio de la web
    path('nosotros', publicacion.views.nosotros, name='nosotros'), # inicio de la web

    path('blog/post/nueva/', publicacion.views.nueva, name='publicacion_nueva'),
    path('blog/post/editar/<int:id>/', publicacion.views.editar, name='publicacion_editar'),
    path('blog/post/eliminar/<int:id>/', publicacion.views.eliminar, name='publicacion_eliminar'),
    path('blog/post/<int:id>/', publicacion.views.ver, name='publicacion_ver'),
    path('blog/post/autor/', publicacion.views.autor, name='publicacion_por_autor'),
    path('blog/post/autor/<int:id>/', publicacion.views.autor, name='publicacion_por_autor'),
    path('blog/post/<int:publicacion_id>/comentario/<int:comentario_id>/', comentario.views.ver, name='comentario_ver'),    

    path('categoria/listado/', categoria.views.listado, name='categoria_listado'),
    path('categoria/nueva/', categoria.views.nueva, name='categoria_nueva'),
    path('categoria/editar/<int:id>/', categoria.views.editar, name='categoria_editar'),
    path('categoria/eliminar/<int:id>/', categoria.views.eliminar, name='categoria_eliminar'),
    path('categoria/<int:id>/', categoria.views.filtrar, name='categoria_filtrar'),

    path('usuario/listado/', cuenta.views.usuario_listado, name="usuario_listado"),
    path('usuario/nuevo/', cuenta.views.usuario_nuevo, name="usuario_nuevo"),
    path('usuario/editar/<int:id>/', cuenta.views.usuario_editar, name="usuario_editar"),
    path('usuario/eliminar/<int:id>/', cuenta.views.usuario_eliminar, name="usuario_eliminar"),
    path('usuario/tipo/', cuenta.views.tipo_listado, name="tipo_listado"),
    path('usuario/tipo/nuevo/', cuenta.views.tipo_nuevo, name="tipo_nuevo"),
    path('usuario/tipo/editar/<int:id>', cuenta.views.tipo_editar, name="tipo_editar"),
    path('usuario/tipo/eliminar/<int:id>', cuenta.views.tipo_eliminar, name="tipo_eliminar"),

    path('cuenta/', cuenta.views.cuenta, name="cuenta"),
    path('cuenta/registrar/', cuenta.views.registrar, name="cuenta_registrar"),
    path('cuenta/iniciar/', cuenta.views.iniciar_sesion, name="iniciar_sesion"),
    path('cuenta/cerrar/', cuenta.views.cerrar_sesion, name="cerrar_sesion"),
    path('cuenta/cambiarPassword/', cuenta.views.cambiarPassword, name="cambiarPassword"),
    
    path('restringido/', cuenta.views.restringido, name='restringido'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
