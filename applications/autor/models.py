from django.db import models
from django_prose_editor.fields import ProseEditorField
from django_prose_editor.sanitized import SanitizedProseEditorField
from .managers import AutorManager

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField(default=0)


    def __str__(self):
        return str(self.id) + '-' +self.nombre + ' ' + self.apellidos

    class Meta:
        abstract = True


class Autor(Persona):
    seudonimo = models.CharField('Seudónimo', max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    reseña = ProseEditorField(blank=True, null=True)
    objects = AutorManager()

    class Meta:
        verbose_name = 'Catálogo de Autores'
        verbose_name_plural = 'Catálogo de Autores'
        ordering = ['nombre']


