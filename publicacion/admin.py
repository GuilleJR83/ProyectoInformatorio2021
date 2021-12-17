from django.contrib import admin

# Register your models here.

from .models import Publicacion, Comentario, Like

admin.site.register(Publicacion)

admin.site.register(Comentario)
admin.site.register(Like)

