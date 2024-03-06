from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_text = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Primer nombre", required=False)
    last_name = forms.CharField(label= "Último nombre", required=False)
  

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

        help_text = {k: "" for k in fields}


from users.models import Avatar
from django.core.exceptions import ValidationError
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')

        if imagen is None or imagen == '':
            raise ValidationError("Una imagen es requerida.")

        return imagen
    
        
