from django.contrib import admin
from django.urls import path

from . import views

app_name = 'lector_app'

urlpatterns = [
    path('lectores/', views.ListLectores.as_view(), name='lectores'),
    path('nuevo-lector/', views.NewLectorView.as_view(), name='nuevo_lector'),
    path('lector-detalle/<pk>', views.LectorDetailView.as_view(), name='lector_detalle'),
    path('lector-editar/<pk>', views.LectorUpdateView.as_view(), name='lector_editar'),
    path('lector-borrar/<pk>', views.LectorDeleteView.as_view(), name='lector_borrar'),
    path('add-prestamo/', views.AddPrestamo.as_view(), name='add_prestamo'),
    path('multi-prestamo/', views.AddMultiPrestamo.as_view(), name='multi_prestamo'),
    path('control-prestamo/', views.ListPrestamos.as_view(), name='control_prestamo'),
    path('prestamo-update/<pk>', views.PrestamoUpdateView.as_view(), name='prestamo_update'),
]