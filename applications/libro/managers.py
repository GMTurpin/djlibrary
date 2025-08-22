import datetime
from django.db import models
from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):
    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha_publicacion__range=('1100-01-01', '2200-12-31')
        )
        return resultado

    def listar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(
            titulo__trigram_similar=kword,
            )
            return resultado
        else:
            return self.all()


    def listar_libros2(self, kword, fdesde, fhasta):
        date1 = datetime.datetime.strptime(fdesde, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(fhasta, '%Y-%m-%d')
        resultado = self.filter(
            titulo__icontains=kword,
            fecha_publicacion__range=(date1, date2)
        )
        return resultado

    def libros_categoria(self, categoria):
        if categoria == '0':
            return self.all()
        else:
            resultado = self.filter(categoria__nombre__icontains=categoria).order_by('titulo')
        return resultado

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=Count('libro_prestamo'),

        )
        for r in resultado:
            print('**************************')
            print(r, r.num_prestados)
        return resultado


    def libros_del_autor(self, autor):
        return self.filter(autores__id=autor)


class CategoriaManager(models.Manager):
    def categoria_por_autor(self, autor):
        return self.filter(categoria_libro__autores__id=autor).distinct()

    def categoria_books(self):
        resultado = self.annotate(
            num_libros=Count('categoria_libro')
        )
        for cat in resultado:
            print('**************************')
            print(cat, cat.num_libros)
        return resultado