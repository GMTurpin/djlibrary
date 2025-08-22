from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from .models import Autor
from .forms import NewAutorForm
from ..libro.models import Libro



# Create your views here.
class IndexView(TemplateView):
    template_name = 'inicio.html'


class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'
    paginate_by = 6

    def get_queryset(self):
        word_clave = self.request.GET.get('kword', '')
        return Autor.objects.buscar_autor2(word_clave)

class NewAutorView(CreateView):
    model = Autor
    template_name = 'autor/new_autor.html'
    form_class = NewAutorForm
    success_url = reverse_lazy('autor_app:autores')

    def form_valid(self, form):
        autor = form.save(commit=False)
        autor.save()
        return super(NewAutorView, self).form_valid(form)

class AutorDetailView(DetailView):
    model = Autor
    template_name = "autor/vista.html"

    def get_context_data(self, **kwargs):
        context =super(AutorDetailView,self).get_context_data(**kwargs)
        context['libros_del_autor'] = Libro.objects.filter(autores=self.object)
        return context

class AutorUpdateView(UpdateView):
    template_name = 'autor/update.html'
    model = Autor
    form_class = NewAutorForm
    success_url = reverse_lazy('autor_app:autores')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor/delete.html'
    success_url = reverse_lazy('autor_app:autores')

