from django.shortcuts import render, redirect
from .forms import FormEquipo
from .models import Equipo


def index(request):
    return render(request, 'equiposApp/index.html')

def actualizarEquipo(request, id):
    proyectos = Equipo.objects.get(id = id)
    form = FormEquipo(instance=proyectos)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=proyectos)
        if form.is_valid():
            form.save()
            return redirect('../equipos/')
    data = {'form' : form}
    return render(request, 'equiposApp/agregarEquipo.html', data)


def eliminarEquipo(request, id):
    proyectos = Equipo.objects.get(id = id)
    print(id)
    proyectos.delete()
    return redirect('../equipos/')


def agregarEquipo(request):
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')  
    else:
        form = FormEquipo()
    
    data = {'form': form}
    return render(request, 'equiposApp/agregarEquipo.html', data)


def listadoEquipos(request):
    equipos = Equipo.objects.all()
    data = {'equipos' : equipos}
    return render (request, 'equiposApp/equipos.html' , data)