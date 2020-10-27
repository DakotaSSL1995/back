from django.shortcuts import render, redirect
from .models import Pregunta
from .forms import PreguntaForm

def faq(request):
    preguntas = Pregunta.objects.all()
    data = {
        'preguntas':preguntas
    }

    return render(request,'core/faq.html', data)

def capsula(request):

    return render(request, 'core/capsula.html')

def faq_nueva(request):
    data = {
        'form':PreguntaForm()
    }
    if request.method == 'POST':
        formulario = PreguntaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
    return render(request, 'core/faq_nueva.html', data)
    
def faq_modificar(request, id):
    pregunta = Pregunta.objects.get(id=id)
    data = {
        'form': PreguntaForm(instance=pregunta)
    }
    if request.method == 'POST':
        formulario = PreguntaForm(data=request.POST, instance=pregunta)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/faq_modificar.html', data)


def adminfaq(request):
    preguntas = Pregunta.objects.all()
    data = {
        'preguntas':preguntas
    }

    return render(request,'core/adminfaq.html', data)

def faq_eliminar(request, id):
    pregunta = Pregunta.objects.get(id=id)
    pregunta.delete()
    return redirect(to="adminfaq")