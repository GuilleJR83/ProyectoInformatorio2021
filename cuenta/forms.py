# Importamos los formularios predefinidos que ya trae Django
from django import forms
from django.contrib.auth.models import User, Group
from django.forms import widgets

# Importamos el modelo Usuario que creamos
from cuenta.models import Usuario

# Importamos formularios predefinidos de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm

from django.core.exceptions import ValidationError

# Definimos la clase que mostrará los campos que queremos rellenar al momento de registra un nuevo usuario
class CuentaNuevaForm(UserCreationForm): # Que tiene como clase base <UserCreationForm>
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')

    class Meta:
        model = Usuario # Que tome como modelo la clase <Usuario> que creamos y heredamos de <User>

        # FIELDS permite especificar los campos a mostrar, pero a su vez, 
        # nos ahorra el trabajo de tener que espeficicar si es numerico, texto, etc., entre otras cosas
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', ) # Definimos campos a mostrar en el form de registro

class UsuarioNuevoForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')

    class Meta:
        model = Usuario # Que tome como modelo la clase <Usuario> que creamos y heredamos de <User>
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'groups')
        labels = {'groups': 'Tipo'}

class UsuarioEditarForm(UserChangeForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), label='Tipo')

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'groups')
        widgets = {'groups': forms.SelectMultiple(attrs={'class': 'form-control', }, ), }

class UsuarioEliminarForm(forms.ModelForm):
   class Meta:
       model = Usuario
       fields = ("username", )

# Definimos la clase que mostrará el formulario de inicio de sesión (login)
class IniciarSesionForm(AuthenticationForm): # heredado de AuthenticationForm
    class Meta:
         model = Usuario # modelo
         fields = ['username', 'password'] # campos
         widgets = {'password': forms.PasswordInput(), }

    def confirm_login_allowed(self, user): # no sé cómo hacer para que "pase" por aquí
        if not user.is_active:
            raise forms.ValidationError('Esta cuenta está deshabilitada por el administrador.', code='inactive', )

# Definición de la clase form para el cambio de contraseña
class CambiarPasswordForm(PasswordChangeForm):
    class Meta:
        model = Usuario
        #widgets = {'old_password': forms.PasswordInput(class='form-control'), }
