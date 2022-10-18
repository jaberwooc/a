from email import message
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"home/index.html",{})



def resgister (request):
    if request.method == 'POST':
        form = employeescreateform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'username{username} creado')
            return redirect(index)

    else:
        form = employeescreateform()
    
  
    return render(request,'home/register.html',{'form':form})