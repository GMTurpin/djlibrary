import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django_prose_editor.fields import ProseEditorField
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    objects = CategoriaManager()

    class Meta:
        verbose_name = 'Lista de categoria'
        verbose_name_plural = 'Lista de categorias'
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField(verbose_name='Fecha de publicacion')
    sinopsis = ProseEditorField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    visitas = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    objects = LibroManager()

    class Meta:
        verbose_name = 'Catálogo de Libro'
        verbose_name_plural = 'Catálogo de Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
