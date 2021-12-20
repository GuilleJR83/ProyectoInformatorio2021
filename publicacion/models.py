from django.db import models

from categoria.models import Categoria
from comentario.models import *
from cuenta.models import Usuario

class Publicacion(models.Model):
    # Definición de claves foráneas
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #voto = models.ForeignKey(Voto, on_delete=models.DO_NOTHING) # Like

    # Definición de los campos/atributos
    titulo = models.CharField(max_length=100, blank=False) #blank determina que si o si se escriba algo
    contenido = models.TextField(blank=False)
    imagen = models.FileField() #, blank=True, upload_to='media'
    fechaCreacion = models.DateTimeField(auto_now_add=True) # auto_created=True # 
    fechaEdicion = models.DateTimeField(auto_now=True) # editable=False # 

    # Definición de propiedades y métodos
    def __str__(self):
        return self.titulo
    
    # def getComentarios(self):
    #     return Comentario.objects.filter(publicacion=self.id)

    # @property
    # def Id(self):
    #     return self.id

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username