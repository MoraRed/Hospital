from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitasView, HistoriaClinicaView, MedicosListView

urlpatterns = [
    path('api/citas/', CitasView.as_view(), name='citas'),
    path('api/historia/', HistoriaClinicaView.as_view(), name='historia'),
    path('api/medicos/', MedicosListView.as_view(), name='medicos'),
]