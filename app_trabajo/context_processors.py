from django.contrib.auth.context_processors import auth
from users.models import Avatar
from django.conf import settings


def custom_user(request):
    context = auth(request)
    user = context['user']

    if user.is_authenticated:
        imagen = Avatar.objects.filter(user=request.user.id)
        cant = len(imagen)
        if cant > 0:
            context['user_avatar'] = imagen[cant-1]
        else:
            context['user_avatar'] = settings.MEDIA_URL + "inicial.jpg"

    return context