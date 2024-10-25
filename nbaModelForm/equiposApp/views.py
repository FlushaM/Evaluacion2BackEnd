from django.shortcuts import render, redirect
from .forms import FormEquipo
from .models import Equipo


def index(request):
    return render(request, 'Equipo/index.html')

def actualizarEquipo(request, id):
    proyectos = Equipo.objects.get(id = id)
    form = FormEquipo(instance=proyectos)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=proyectos)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Equipo/agregarEquipo.html', data)


def eliminarEquipo(request, id):
    proyectos = Equipo.objects.get(id = id)
    print(id)
    proyectos.delete()
    return redirect('../equipos/')