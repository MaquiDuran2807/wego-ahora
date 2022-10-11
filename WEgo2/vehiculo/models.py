from django.db import models

# Create your models here.
class Vehiculo (models.Model):
    modelo = models.IntegerField()
    nombre_vehiculo = models.CharField( max_length=50)
    
    
    
class ReferenciaVehiculo (models.Model):
    nombre_referencia = models.CharField( max_length=50)
    
    
class MarcaVehiculo (models.Model):
    nombre_marca = models.CharField( max_length=50)
    
