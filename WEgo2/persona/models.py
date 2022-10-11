from email.policy import default
from secrets import choice
from django.db import models

# Create your models here.
class Persona (models.Model):
    Generos = (
        ('0','Masculino'),
        ('1','Femenino'),
        ('2','Otro')
        
    )
    nombre = models.CharField (max_length=70)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField( max_length=2,choices=Generos,default='0')
    cedula = models.IntegerField()
    foto_persona = models.ImageField( upload_to="media", height_field=None, width_field=None, max_length=None)
    numero_telefono = models.IntegerField()
    correo = models.EmailField(max_length=254)
    
    
    class Meta: 
        verbose_name = "Persona"
        verbose_name_plural = "Personas" #nombre en admin en plural
        
    def __str__ (self):
        return self.nombre + self.apellidos
    
    
class TipoUsuario (models.Model):
    codigo_referido = models.CharField( max_length=50)