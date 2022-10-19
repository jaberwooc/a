from email import message
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login/')
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



