# Importamos el modelo User que vamos a heredar para crear nuestras cuentas de usuarios.
from django.contrib.auth.models import AbstractUser

# Definimos el modelo Usuario el cual utilizaremos para iniciar sesión, publicar post, editarlos, etc.
class Usuario(AbstractUser):
    # El modelo de usuario por defecto a usar por Django en todo el proyecto es este, 
    # y está definido en blog.settings.AUTH_USER_MODEL.

    def __str__(self):
        return self.get_username()
    
    # Devuelve el nombre del grupo al cuál pertenece (Admin/Escritor/Lector)
    def getTipo(self):
        if self.esAdministrador:
            return 'Administrador'
        elif self.esEscritor:
            return 'Escritor'

        return 'Lector'

    # Devuelve True si el usuario pertenece al grupo <Administrador>.
    @property
    def esAdministrador(self):
        return self.groups.filter(name = 'Administrador').exists()
    
    # Devuelve True si el usuario pertenece al grupo <Escritor>.
    @property
    def esEscritor(self):
        return self.groups.filter(name = 'Escritor').exists() # return True #
    
    # Devuelve True si el usuario pertenece al grupo <Lector>.
    @property
    def esLector(self):
        return self.groups.filter(name = 'Lector').exists()
