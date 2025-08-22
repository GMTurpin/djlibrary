from django import forms
from .models import Lector, Prestamo
from applications.libro.models import Libro

class NewLectorForm(forms.ModelForm):

    class Meta:
        model = Lector
        fields = ['nombre', 'apellidos', 'nacionalidad', 'telefono', 'edad']
        widgets = {
            'edad': forms.NumberInput(attrs={'size': 4})
        }


class PrestamoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libro'].queryset = self.fields['libro'].queryset.filter(stock__gte=1)


    class Meta:
        model = Prestamo
        fields = ['lector', 'libro']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }


class MultiPrestamoForm(forms.ModelForm):
    libros = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Prestamo
        fields = ['lector']

    def __init__(self, *args, **kwargs):
        super(MultiPrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.filter(stock__gte=1)


class EditPrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields =  ['libro','lector','fecha_prestamo', 'fecha_devolucion', 'vencimiento']

    def __init__(self, *args, **kwargs):
        super(EditPrestamoForm, self).__init__(*args, **kwargs)


