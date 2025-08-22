from django.db import models
from applications.libro.models import Libro
from applications.autor.models import Persona
from .managers import PrestamoManager, LectorManager


# Create your models here.
class Lector(Persona):
    telefono = models.CharField(max_length=15)
    objects = LectorManager()

    class Meta:
        verbose_name = 'Catálogo de Lector'
        verbose_name_plural = 'Catálogo de Lectores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre + ' ' + self.apellidos


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField(verbose_name='Fecha de prestamo')
    vencimiento = models.DateField(verbose_name='Fecha de vencimiento', blank=True, null=True)
    fecha_devolucion = models.DateField(verbose_name='Fecha de devolucion', blank=True, null=True)
    devuelto = models.BooleanField(default=False)
    objects = PrestamoManager()

    class Meta:
        verbose_name = 'Control de Prestamos'
        verbose_name_plural = 'Control de Prestamos'
        ordering = ['fecha_prestamo']

    def __str__(self):
        return self.libro.titulo
