from django.db import models

# Create your models here.
class Persona(models.Model):
    fullname = models.CharField('Nombre',max_length=100)
    pais = models.CharField('Pais',max_length=30)
    pasaporte = models. CharField('Pasaporte',max_length=50)
    edad = models.PositiveIntegerField('Edad')
    nickname = models.CharField('Nickname',max_length=10)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['fullname']
#        db_table = 'persona'
        unique_together = ['pais','nickname']
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_minima'),
        ]
        abstract = True

    def __str__(self):
        return self.fullname

class Empleado(Persona):
    empleo = models.CharField('Empleo',max_length=50)

class Cliente(Persona):
    email = models.EmailField('Email')