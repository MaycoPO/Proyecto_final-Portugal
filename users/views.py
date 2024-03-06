from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def login_request(request):
    

   

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "app_trabajo/index.html")
        
        
        
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def register(request):

    

    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, "app_trabajo/index.html")
        
    else:

        form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form})

from users.forms import UserEditForm

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data


            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"] 
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.save()

            return render(request, "app_trabajo/index.html")

    else:

        datos = {
            'last_name': usuario.last_name,
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})

from users.forms import AvatarFormulario
from users.models import Avatar
from django.contrib.auth.models import User

@login_required
def agregar_avatar(request):

    if request.method == "POST":
        mi_form = AvatarFormulario(request.POST, request.FILES)

        if mi_form.is_valid():
            user = User.objects.get(username=request.user)
            try:
                avatar = Avatar.objects.get(user=user)
            except Avatar.DoesNotExist:
                avatar = Avatar(user=user, imagen = mi_form.cleaned_data['imagen'])
            else:
                avatar.imagen = mi_form.cleaned_data['imagen']

            
            avatar.save()

            return render(request, "app_trabajo/index.html")
        
    else:
        mi_form = AvatarFormulario()

    context_data = {"mi_form": mi_form}
    return render(request, 'users/agregar_avatar.html', context_data)



