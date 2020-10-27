from django.contrib import admin
from .models import Pregunta, Pregunta_Categoria

admin.site.register(Pregunta_Categoria)
admin.site.register(Pregunta)
