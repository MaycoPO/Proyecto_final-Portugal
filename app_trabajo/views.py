from django.shortcuts import render
from .models import electrodomesticos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Avatar

def inicio(request):
    try:

     avatares = Avatar.objects.get(user=request.user.id)
     imagen = avatares.imagen.url
    except:
         imagen = ""
    return render(request, "app_trabajo/index.html", {"url": imagen})

def about(request):
     return render(request, 'app_trabajo/about.html')



class electrodomes_ListView(LoginRequiredMixin, ListView):
      model = electrodomesticos
      template_name = "app_trabajo/electrodomestico_lista.html"


class electrodomes_CreateView(LoginRequiredMixin, CreateView):

      model = electrodomesticos
      template_name = "app_trabajo/electrodomestico_form.html"
      success_url = "/inicio/"
      fields = ["electrodomestico", "modelo", "compra", "cliente", "DNI"]

class electrodomes_DetailView(LoginRequiredMixin, DetailView):
     model = electrodomesticos
     template_name = "app_trabajo/electrodomestico_detalle.html"
     
class electrodomes_UpdateView(LoginRequiredMixin, UpdateView):
     model = electrodomesticos
     template_name = "app_trabajo/electrodomestico_form.html"
     success_url = "/inicio/electrodomesticos/lista"
     fields = ["electrodomestico", "modelo", "compra"]
     
class electrodomes_DeleteView(LoginRequiredMixin, DeleteView):
     model = electrodomesticos
     template_name = "app_trabajo/electrodomestico_eliminar.html"
     success_url = "/inicio/electrodomesticos/lista"

