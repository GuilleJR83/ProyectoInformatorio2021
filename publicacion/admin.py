from django.contrib import admin
from publicacion.models import Publicacion

from .models import Publicacion, Comentario, Like

admin.site.register(Publicacion)

admin.site.register(Comentario)
admin.site.register(Like)