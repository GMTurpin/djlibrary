from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Libro, Categoria
from ..lector.models import Prestamo
from .forms import NewLibroForm

# Create your views here.

class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'
    paginate_by = 6

    def get_queryset(self):
        word_clave = self.request.GET.get('kword', '')
        #fecha_desde
        fdesde = self.request.GET.get('fecha_desde', '')
        #fecha-hasta
        fhasta = self.request.GET.get('fecha_hasta', '')

        if fdesde and fhasta:
            return Libro.objects.listar_libros2(word_clave, fdesde, fhasta)
        else:
            return Libro.objects.listar_libros(word_clave)


class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'
    paginate_by = 6

    def get_queryset(self):
        word_clave = self.request.GET.get('kword', '')
        return Libro.objects.listar_libros_trg(word_clave)


class ListLibrosCat(ListView):
    context_object_name = 'lista_cats'
    template_name = 'libro/lista_cats.html'
    paginate_by = 20

    def get_context_data(self, **kwargs    ):
        context = super(ListLibrosCat, self).get_context_data(**kwargs)
        context['box_cats'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        nombre_cat = self.request.GET.get('kword', '')
        return Libro.objects.libros_categoria(nombre_cat)


class ListPrestamosLibro(ListView):
    model = Libro
    context_object_name = 'historial'
    template_name = 'libro/list_prestado.html'

    def get_context_data(self, **kwargs):
        context = super(ListPrestamosLibro, self).get_context_data(**kwargs)
        context['libro'] = Libro.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        queryset = Prestamo.objects.filter(libro=self.kwargs['pk']).order_by('fecha_prestamo')
        return queryset



class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"


class NewLibroView(CreateView):
    model = Libro
    template_name = 'libro/newbook.html'
    form_class = NewLibroForm
    success_url = reverse_lazy('libro_app:libros')

    def form_valid(self, form):
        libro = form.save(commit=False)
        libro.save()
        return super(NewLibroView, self).form_valid(form)


class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'libro/update_book.html'
    form_class = NewLibroForm
    success_url = reverse_lazy('libro_app:libros')

    def form_valid(self, form):
        libro = form.save(commit=False)
        libro.save()
        return super(LibroUpdateView, self).form_valid(form)


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libro/delete_libro.html'
    success_url = reverse_lazy('libro_app:libros')

