from tokenize import group
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class employees(models.Model):
    id_empleado = models.BigIntegerField()
    nombre_empleado = models.CharField(max_length=256)
    fecha_de_contratacion = models.DateField()
    RFC = models.CharField(max_length=256)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    



    def __str__(self):
        return self .nombre_empleado 
  

class piezas(models.Model):
    descripcion  = models.CharField(max_length=256)
    estado =  models.CharField(max_length=256)

    def __str__(self):
        return self .descripcion


