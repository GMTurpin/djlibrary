from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        ).order_by('nombre')
        return resultado


    def buscar_autor3(self, kword):
        resultado = self.filter(nombre__icontains=kword
        ).exclude(
            Q(edad__icontains=79) | Q(edad__icontains=82)
        )
        return resultado


    def buscar_autor4(self, kword):
        resultado = self.filter(edad__gt=60, edad__lt=80).order_by('id')
        return resultado