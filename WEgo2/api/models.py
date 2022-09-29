from django.db import models

# Create your models here.
class account (models.Model):
    generos = (  ('1','Masculino'),
                ('2','Femenino'),
                ('3','Otro')
            )
    nombre_persona = models.CharField('Nombre', max_length=50)
    apellido_persona = models.CharField('Apellido', max_length=50)
    genero = models.CharField('Genero', max_length=3,choices=generos)
    cedula_persona = models.PositiveBigIntegerField()
    celular_persona = models.IntegerField()
    foto_persona = models.ImageField('Foto', upload_to='media', height_field=None, width_field=None, max_length=None)
    correo = models.EmailField('Correo',max_length=50)
    rol_persona = models.BooleanField(default=False)