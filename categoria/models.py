from django.db import models

class Categoria(models.Model):
    #id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=False, null=False, unique=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaEdicion = models.DateTimeField(auto_now=True)

    # Definición de propiedades y métodos
    def __str__(self):
        return self.descripcion
