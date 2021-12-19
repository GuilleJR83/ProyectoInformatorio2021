from django.db import models

from categoria.models import Categoria
from comentario.models import *
from cuenta.models import Usuario

class Publicacion(models.Model):
    # Definición de claves foráneas
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #comentario = models.ForeignKey(Comentario, on_delete=models.DO_NOTHING)
    #voto = models.ForeignKey(Voto, on_delete=models.DO_NOTHING) # Like

    # Definición de los campos/atributos
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False) #blank determina que si o si se escriba algo
    contenido = models.TextField(blank=False)
    destacado = models.BooleanField(default=False)
    imagen = models.ImageField(blank=True)
    #slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
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