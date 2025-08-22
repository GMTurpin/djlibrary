from django.contrib import admin
from .models import Libro, Categoria


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'stock')
    search_fields = ('titulo', 'autores__nombre', 'autores__apellidos')
    list_filter = ('categoria', 'autores','stock')
    filter_horizontal = ('autores',)
    list_per_page = 10



# Register your models here.

admin.site.register(Libro, LibroAdmin)
admin.site.register(Categoria)

title = 'Administrador de Libros'
subtitle = 'Gestor de Biblioteca'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
