from django.db import models

# Create your models here.
class Conductor (models.Model):
    licencia = models.IntegerField()
    foto_licencia = models.ImageField( upload_to="media", height_field=None, width_field=None, max_length=None)
    foto_conductor = models.ImageField( upload_to="media", height_field=None, width_field=None, max_length=None)
    antecedentes = models.CharField( max_length=50)
    
    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores" #nombre en admin en plural
        
    