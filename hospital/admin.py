from django.contrib import admin
from .models import Doctor, Paciente, HistoriaClinica, Cita

admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(HistoriaClinica)
admin.site.register(Cita)