from django.contrib.auth.models import Group

from categoria.models import Categoria
#from cuenta.models import Usuario
#from publicacion.models import Publicacion

# PROCESADORES DE CONTEXTO
# Nos permitirá tener a mano en todos los template HTML, los contextos que definamos abajo.

def procesadores_contexto(request):
    return {
                'categorias': Categoria.objects.all(),
                'grupos': Group.objects.all(),
            }
