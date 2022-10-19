from tkinter import CASCADE
from tokenize import group
from unittest.util import _MAX_LENGTH
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
    id_piezas = models.BigIntegerField()
    descripcion  = models.CharField(max_length=256)
    cantidad_piezas = models.BigIntegerField()

    def __str__(self):
        return self .descripcion

class orden_piezas(models.Model):
    id_orden = models.BigIntegerField()
    nombre_empleado = models.ForeignKey(employees, on_delete= models.CASCADE)
    nombre_empleado = models.ForeignKey(employees, on_delete= models.CASCADE)
    fecha_hora = models.DateTimeField()
    descripcion = models.OneToOneField(piezas, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return str(self.id_orden)



