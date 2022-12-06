from django.shortcuts import render
from .models import Proyect
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render (request,'home.html')

def proyectos(request):
    projects=Proyect.objects.all()
    return render (request, 'proyectos.html',{'projects':projects} )    