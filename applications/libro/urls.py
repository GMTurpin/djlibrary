from django.contrib import admin
from django.urls import path

from . import views
app_name = 'libro_app'

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-trg/', views.ListLibrosTrg.as_view(), name='libros_trg'),
    path('libros-cat/', views.ListLibrosCat.as_view(), name='libros_cat'),
    path('libro-detalle/<pk>', views.LibroDetailView.as_view(), name='libro_detalle'),
    path('libro-nuevo/', views.NewLibroView.as_view(), name='libro_nuevo'),
    path('libro-editar/<pk>', views.LibroUpdateView.as_view(), name='libro_editar'),
    path('libro-borrar/<pk>', views.LibroDeleteView.as_view(), name='libro_borrar'),
    path('lista-prestamos/<pk>', views.ListPrestamosLibro.as_view(), name='lista_prestamos'),
]