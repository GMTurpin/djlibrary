from django.contrib import admin
from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad', 'nacionalidad', 'seudonimo')
    search_fields = ('nombre', 'apellidos', 'nacionalidad', 'seudonimo')
    list_filter = ('nacionalidad', 'edad', 'seudonimo')
    list_per_page = 6

    class Meta:
        model = Autor
        fields = '__all__'
        verbose_name = 'Autores'

# Register your models here.

admin.site.register(Autor, AutorAdmin)