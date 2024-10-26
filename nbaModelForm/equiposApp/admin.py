from django.contrib import admin
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'campeonatos', 'conferencia', 'estadio', 'colores', 'liga']
admin.site.register(Equipo, EquipoAdmin)