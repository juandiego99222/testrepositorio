from django.shortcuts import render
from .models import Projecto



# Create your views here.

def portafolio(request):

    projects= Projecto.objects.all()
    return render(request, "portfolio/portafolio.html", {'projects':projects}) 

# vista-template, asignar proyectos a la vista portafolio