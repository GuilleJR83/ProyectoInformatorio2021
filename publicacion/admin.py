from django.contrib import admin

from comentario.models import Comentario
from .models import Publicacion, Like

admin.site.register(Publicacion)
admin.site.register(Like)
#admin.site.register(Comentario)
