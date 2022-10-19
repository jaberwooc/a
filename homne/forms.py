from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User



class employeescreateform(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)
    id_empleado =  forms.IntegerField(initial=450)
    nombre_empleado = forms.CharField(max_length=256)
    fecha_de_contratacion = forms.DateField()
    RFC = forms.CharField(max_length=256)
    hora_entrada = forms.TimeField()
    hora_salida = forms.TimeField()
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
 