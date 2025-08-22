from django.contrib import admin
from django.urls import path

from . import views

app_name = 'autor_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('autores/', views.ListAutores.as_view(), name='autores'),
    path('nuevo-autor/', views.NewAutorView.as_view(), name='nuevo_autor'),
    path('autor-detalle/<pk>', views.AutorDetailView.as_view(), name='autor_detalle'),
    path('autor-editar/<pk>', views.AutorUpdateView.as_view(), name='autor_editar'),
    path('autor-borrar/<pk>', views.AutorDeleteView.as_view(), name='autor_borrar'),
]