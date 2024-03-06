from django.urls import path
from app_trabajo import views



urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('electrodomesticos/lista', views.electrodomes_ListView.as_view(), name="electrodomesticos_ver"),
    path('electrodomesticos/detalle/<int:pk>/', views.electrodomes_DetailView.as_view(), name="Detalle"),
    path('electrodomesticos/editar/<int:pk>/', views.electrodomes_UpdateView.as_view(), name="Editar"),
    path('electrodomesticos/eliminar/<int:pk>/', views.electrodomes_DeleteView.as_view(), name="Borrar"),
    path('electrodomesticos/crear/', views.electrodomes_CreateView.as_view(), name="Crear"),
    path('acerca_de/', views.about, name="AcercaDeMi")
]
