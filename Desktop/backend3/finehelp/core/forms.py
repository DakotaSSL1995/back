from django import forms
from django.forms import ModelForm
from .models import Pregunta

class PreguntaForm(ModelForm):

    class Meta: 
        model = Pregunta
        fields = ('titulo_pregunta', 'contenido_pregunta', 'pregunta_categoria')