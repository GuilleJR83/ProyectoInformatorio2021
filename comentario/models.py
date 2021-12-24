from django.db import models

#from blog import settings
from cuenta.models import Usuario
from publicacion.models import Publicacion

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fechaComentario = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=250)

    def __str__(self):
        return self.contenido
    
    def getAutor(self):
        return self.autor.get_username()
