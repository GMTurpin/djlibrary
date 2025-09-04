
from django import forms
from .models import Autor

class NewAutorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewAutorForm, self).__init__(*args, **kwargs)
        reseña = self.fields['reseña'].widget.attrs
        reseña['class'] = 'form-control'
        reseña['rows'] = 3


    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'edad', 'reseña','foto']
        widgets = {
            'edad': forms.NumberInput,
        }