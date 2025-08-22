from datetime import date

from django.db import models
from django.db.models import Q, Count, Avg, Sum

class LectorManager(models.Manager):
    def buscar_lector(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        ).order_by('nombre')
        return resultado

class PrestamoManager(models.Manager):
    def libros_prom_edades(self):
        resultado = self.filter(
            libro__id='13'
        ).aggregate(
            prom_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad')
        )
        return resultado

    def listprestamos(self, opcion):
        resultado = self.all()
        if opcion == 'Pendientes':
            resultado = self.filter(devuelto=False)
        if opcion == 'Vencidos':
            resultado = self.filter(vencimiento__lt=date.today())
        if opcion == 'Devueltos':
            resultado = self.filter(devuelto=True)
        return resultado






