from django import forms
from .models import Libro

class NewLibroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewLibroForm, self).__init__(*args, **kwargs)
        sinopsis = self.fields['sinopsis'].widget.attrs
        sinopsis['class'] = 'form-control'
        sinopsis['rows'] = 3

    class Meta:
        model = Libro
        fields = ['titulo', 'categoria', 'autores', 'fecha_publicacion', 'sinopsis','portada', 'stock']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'categoria': forms.Select(),
            'stock': forms.NumberInput,
        }