from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib import messages

from .models import Lector, Prestamo
from .forms import NewLectorForm, PrestamoForm, MultiPrestamoForm, EditPrestamoForm
from ..libro.models import Libro


# Create your views here.

class NewLectorView(CreateView):
    model = Lector
    template_name = 'lector/new_lector.html'
    form_class = NewLectorForm
    success_url = reverse_lazy('lector_app:lectores')

    def form_valid(self, form):
        lector = form.save(commit=False)
        lector.save()
        return super(NewLectorView,self).form_valid(form)


class LectorDetailView(DetailView):
    model = Lector
    template_name = "lector/ficha_lector.html"

    def get_context_data(self, **kwargs):
        context =super(LectorDetailView,self).get_context_data(**kwargs)
        context['libros_del_lector'] = Prestamo.objects.filter(lector=self.object)
        print(self.object)
        return context


class LectorUpdateView(UpdateView):
    model = Lector
    template_name = "lector/edit_lector.html"
    form_class = NewLectorForm
    success_url = reverse_lazy('lector_app:lectores')


class LectorDeleteView(DeleteView):
    model = Lector
    template_name = "lector/delete_lector.html"
    success_url = reverse_lazy('lector_app:lectores')





class ListLectores(ListView):
    context_object_name = 'lista_lectores'
    template_name = 'lector/fichas.html'
    paginate_by = 10

    def get_queryset(self):
        word_clave = self.request.GET.get('kword', '')
        return Lector.objects.buscar_lector(word_clave)


class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = reverse_lazy('lector_app:control_prestamo')

    def get_queryset(self):
        queryset = Libro.objects.filter(stock__gt=0)
        return queryset


    def form_valid(self, form):
        obj, created = Prestamo.objects.get_or_create(
            libro = form.cleaned_data['libro'],
            lector = form.cleaned_data['lector'],
            devuelto=False,
            defaults={
                'fecha_prestamo': date.today(),
                'vencimiento': date.today() + timedelta(days=30),
            }
        )
        if created:
            messages.add_message(self.request, messages.SUCCESS, 'Prestamo exitoso')
            form.cleaned_data['libro'].stock = form.cleaned_data['libro'].stock - 1
            form.cleaned_data['libro'].save()
            return super(AddPrestamo, self).form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR, 'Este lector ya tiene prestado este libro')
            return HttpResponseRedirect('/')


class AddMultiPrestamo(FormView):
    template_name = 'lector/add_multiprestamo.html'
    form_class = MultiPrestamoForm
    success_url = reverse_lazy('lector_app:control_prestamo')

    def form_valid(self, form):
        prestamos = []
        for libro in form.cleaned_data['libros']:
            prestamo = Prestamo(
                libro = libro,
                lector = form.cleaned_data['lector'],
                devuelto = False,
                fecha_prestamo = date.today(),
                vencimiento = date.today() + timedelta(days=30),
            )
            prestamos.append(prestamo)
        Prestamo.objects.bulk_create(prestamos)
        for prestamo in prestamos:
            prestamo.libro.stock = prestamo.libro.stock - 1
            prestamo.libro.save()
        return super(AddMultiPrestamo, self).form_valid(form)


class ListPrestamos(ListView):
    context_object_name = 'lista_prestamos'
    template_name = 'lector/list_prestamos.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListPrestamos, self).get_context_data(**kwargs)
        opciones = ['Pendientes', 'Vencidos', 'Devueltos']
        context['opciones'] = opciones
        return context

    def get_queryset(self):
        opselected = self.request.GET.get('listopciones', '')
        return Prestamo.objects.listprestamos(opselected)


class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = 'lector/update_prestamo.html'
    form_class = EditPrestamoForm
    success_url = reverse_lazy('lector_app:control_prestamo')

    def form_valid(self, form):
        prestamo = form.save(commit=False)
        if prestamo.fecha_devolucion!=None:
            prestamo.libro.stock = prestamo.libro.stock + 1
            prestamo.libro.save()
            prestamo.devuelto = True
        prestamo.save()
        return super(PrestamoUpdateView, self).form_valid(form)




