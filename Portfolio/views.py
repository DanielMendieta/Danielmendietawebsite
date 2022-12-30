from django.shortcuts import render, redirect
from .models import Proyect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def home(request):
    return render (request,'home.html')

def proyectos(request):
    projects=Proyect.objects.all()
    return render (request, 'proyectos.html',{'projects':projects} )    

def formulario(request):
    if request.method=='POST':
        subject = request.POST["asunto"]
        message = request.POST["message"] + " " + request.POST["email"]
        email_from= settings.EMAIL_HOST_USER
        recipient_list = ["mendietadaniel1994@gmail.com"]
        send_mail (subject, message, email_from, recipient_list)
        messages.success(request,'Tu correo ha sido enviado gracias❤')
        return render (request, 'formulario.html')

    return render(request, 'formulario.html')    
