from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    seguro_social = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50, unique=True, default='valor_por_defecto')

    def __str__(self):
        return self.nombre

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_visita = models.DateField()
    notas = models.TextField()
    diagnostico = models.CharField(max_length=255)
    tratamiento = models.TextField()

    def __str__(self):
        return f"{self.paciente} visitado el {self.fecha_visita}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita para {self.paciente} con {self.doctor} el {self.fecha_cita}"
