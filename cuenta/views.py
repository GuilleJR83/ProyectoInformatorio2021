# Importamos RENDER y REDIRECT
from django.shortcuts import render, redirect

# Importamos los formularios que creamos en /cuenta/forms.py
from cuenta.forms import *

# Importamos los modelos que personalizamos en /cuenta/models.py
from cuenta.models import *

# Importamos funciones de Django que nos permitirán crear/borrar sesiones en el navegador cada vez que hagamos login o logout
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import Group

# Importamos la plantilla ERROR 404
#from django.http.response import Http404

# Mostrará la sección con las opciones de edición de cuenta de usuario.
# Opciones como cambiar clave, cambiar e-mail, nombre/apellido
def cuenta(request):
    perfil = Usuario.objects.get(pk=request.user.id)
    template = 'cuenta/cuenta.html'
    contexto = {'perfil': perfil}

    return render(request, template, contexto)

def restringido(request):
    template = 'cuenta/restringido.html'
    contexto = {}

    return render(request, template, contexto)

# Tipos de usuarios, también llamados Grupos de Django.
def tipo_listado(request):
    listado = Group.objects.all()
    template = 'cuenta/usuario_tipo.html'
    contexto = {'tipos': listado, }

    return render(request, template, contexto)

def tipo_editar(request, id):
    pass

def tipo_eliminar(request, id):
    pass

def tipo_nuevo(request, id):
    pass

# Mostrará el form de registro para un nuevo usuario
def registrar(request):
    if request.method == 'POST':
        form = CuentaNuevaForm(request.POST) # Instanciamos el modelo de FORM que definimos y le asignamos el parámetro <request.POST>
                                             # para que pase los datos que ingresamos para crear el nuevo usuario.
        if form.is_valid(): # verificamos si todos los datos ingresados (principalmente los requeridos, como nombre de usuario, 
                            # email, clave) están y son válidos.
            
            # Sí entra aquí, quiere decir que están bien los datos
            form.save() # Asi que vamos a guardarlos (a registrar el usuario en al base de datos)

            uID = form.cleaned_data.get('username') # rescatamos el nombre de usuario del form
            pwd = form.cleaned_data.get('password1') # obtenemos la contraseña, también del form que rellenamos
            user = authenticate(request, username = uID, password = pwd) # y utilizamos <autenticate> (que es una función de Django) 
                                                                         # para que verifique si el mismo existe en nuestra base de datos.
                                                                         # Si existe, nos devuelve un objecto <Usuario> que lo usamos más abajo

            grp = Group.objects.get(name='Lector') # Una vez registrado el usuario, le damos el grupo por defecto que es <Lector>
            grp.user_set.add(user)

            # Si <autenticate> no encontró el usuario, devuelve <None>
            # Por el contrario, si el usuario se creó, directamente continuamos a iniciar sesión 
            # sin redireccionar al cliente al form de inicio de seción y creamos la sesión.
            if user is not None: # Verificamos que <user> es distinto de <None>, y si es así, creamos una sesión en el navegador
                login(request, user) # creamos la sesión de usuario (<login()> es una función que viene definida en Django)
                return redirect('../') # retornamos una url que nos manda a cuenta/index.html (panel de opciones para el usuario)

        #messages.success(request, 'Cuenta creada exitosamente.')
    else: # Si el método pasado no es POST
        form = CuentaNuevaForm() # mostramos el form vacío para que el cliente lo rellene

    #logger.debug('registrar')

    template = 'cuenta/registrar.html'
    contexto = {'form': form, } # definimos el contexto para usar en el archivo .html
    return render(request, template, contexto) # renderizamos

# def cuenta_creada(request, id):
#     try:
#         usuario = Usuario.objects.get(pk=id)
#     except:
#         raise Http404('La cuenta de usuario no existe.')
    
#     contexto = {'usuario': usuario, }
#     template = 'cuenta/creada.html'

#     return render(request, template, contexto)

# Función que se encargará de crear la sesión para el cliente cuando inicie sesión
def iniciar_sesion(request):
    template = 'cuenta/iniciar.html' # url de la plantilla a usar

    if request.method == 'POST':
        form = IniciarSesionForm(request, data=request.POST)    # Instanciamos el modelo de FORM que definimos 
                                                                # y le asignamos el parámetro <request> y los datos pasados (request.POST)
                                                                # para que pase los datos que ingresamos para iniciar sesión.

        if form.is_valid(): # validamos form
            uID = form.cleaned_data.get('username') # obtenemos nombre
            pwd = form.cleaned_data.get('password') # obtenemos clave
            user = authenticate(request, username = uID, password = pwd) # verificamos (autenticamos) que el usuario existe

            if user is not None: # si existe el usuario...
                #messages.debug(request, '%s ha iniciado sesión.', user.get_username)
                login(request, user) # creamos la sesión en el navegador
                return redirect('index') # redirigimos a panel de usuario
            #else:
                #return render(request, template, {'error_message': 'ASASDAS'})
        
    else: # Si el método pasado no es POST
        form = IniciarSesionForm() # mostramos el form vacío para que el cliente lo rellene

    contexto = {'form': form, }# definimos el contexto para usar en el archivo .html
    return render(request, template, contexto) # renderizamos

# Esta función borrará la sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

# Nos permite cambiar la clave del usuario que actualmente tiene sesión iniciada en el navegador.
def cambiarPassword(request):
    if request.method == 'POST':
        form = CambiarPasswordForm(request.user, request.POST)  # este form requiere que le pasemos los datos del usuario 
                                                                # al que vamos a modificar su contraseña mediante <request.user>

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # actualiza la sesión actual con la nueva contraseña del ususario
            return redirect('perfil')
    else:
        form = CambiarPasswordForm(request.user) # cargamos el form con los datos del usuario que se modificará
    
    template = 'cuenta/cambiarPassword.html'
    contexto = {'form': form, }
    return render(request, template, contexto)

def usuario_listado(request):
    listado = Usuario.objects.all()
    template = 'cuenta/usuario_listado.html'
    contexto = {'usuarios': listado, }

    return render(request, template, contexto)

def usuario_editar(request, id):
    u = Usuario.objects.get(pk=id)
    form = UsuarioEditarForm(request.POST or None, instance=u)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('usuario_listado')

    template = 'cuenta/usuario_editar.html'
    contexto = {'form': form, 'usuario': u, }

    return render (request, template, contexto)

# Mostrará el form de registro para un nuevo usuario
def usuario_nuevo(request):
    if request.method == 'POST':
        form = UsuarioNuevoForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.save()
            #grp = Group.objects.get(pk=form.cleaned_data['groups'])
            #grp.user_set.add(user)
            return redirect('usuario_listado')
    else:
        form = UsuarioNuevoForm()

    contexto = {'form': form, }
    return render(request, 'cuenta/usuario_nuevo.html', contexto)

def usuario_eliminar(request, id):
    usuario = Usuario.objects.get(pk=id)
    form = UsuarioEliminarForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_listado') # debe retornar al mismo lugar en el que estaba

    template = 'cuenta/usuario_eliminar.html'
    contexto = {'form': form, 'usuario': usuario}
    return render (request, template, contexto)
