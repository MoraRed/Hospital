# Importaciones de Django y Django REST Framework
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

# Importaciones de modelos y serializadores
from .models import Doctor, Paciente, HistoriaClinica, Cita
from .serializers import DoctorSerializer, PacienteSerializer, HistoriaClinicaSerializer, CitaSerializer

# Importaciones estándar de Python
import datetime

class CitasView(APIView):
    def get(self, request):
        cedula = request.query_params.get('cedula')
        if cedula is None:
            return Response({"error": "No se proporcionó el número de cédula"}, status=status.HTTP_400_BAD_REQUEST)

        # Correctamente filtrar usando el campo relacionado
        citas = Cita.objects.filter(paciente__cedula=cedula).order_by('fecha_cita')

        if citas.exists():
            serializer = CitaSerializer(citas, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No hay citas programadas"}, status=status.HTTP_404_NOT_FOUND)
        
class HistoriaClinicaView(APIView):

    def get(self, request):
        cedula = request.query_params.get('cedula')
        if cedula is None:
            return Response({"error": "No se proporcionó el número de cédula"}, status=status.HTTP_400_BAD_REQUEST)

        historia = HistoriaClinica.objects.filter(paciente__cedula=cedula).order_by('-fecha_visita')
        if historia.exists():
            serializer = HistoriaClinicaSerializer(historia, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No se encontró la historia clínica"}, status=status.HTTP_404_NOT_FOUND)

class MedicosListView(APIView):
    def get(self, request):
        medicos = Doctor.objects.all().order_by('especialidad')
        serializer = DoctorSerializer(medicos, many=True)
        return Response(serializer.data)