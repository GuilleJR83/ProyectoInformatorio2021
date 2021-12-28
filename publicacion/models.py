from django.db import models

from categoria.models import Categoria
#from comentario.models import *
from cuenta.models import Usuario

class Publicacion(models.Model):
    # Definición de claves foráneas
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Definición de los campos/atributos
    titulo = models.CharField(max_length=100, blank=False) #blank determina que si o si se escriba algo
    contenido = models.TextField(blank=False)
    imagen = models.FileField() #, blank=True, upload_to='media'
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaEdicion = models.DateTimeField(auto_now=True)

    # Definición de propiedades y métodos
    def __str__(self):
        return self.titulo
    
    def getCountComentarios(self):
        return self.comentario_set.all().count()
    
    def getCountLikes(self):
        return self.like_set.all().count()

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
