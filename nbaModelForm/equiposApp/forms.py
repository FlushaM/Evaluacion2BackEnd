from django import forms
from .models import Equipo


class FormEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
