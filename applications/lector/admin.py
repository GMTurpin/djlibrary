from django.contrib import admin
from .models import Lector, Prestamo

# Register your models here.

class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'apellidos', 'nacionalidad')
    list_filter = ('nacionalidad', 'edad')
    list_per_page = 6

    class Meta:
        model = Lector
        fields = '__all__'
        verbose_name = 'Lectores'

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'lector', 'fecha_prestamo', 'fecha_devolucion', 'vencimiento', 'devuelto')
    search_fields = ('libro', 'lector')
    list_filter = ('libro', 'lector', 'devuelto')
    list_per_page = 10


admin.site.register(Lector, LectorAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.site_header = 'Administrador de Biblioteca'