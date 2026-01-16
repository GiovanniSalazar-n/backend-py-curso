import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

from .clases import Alumno, Curso  


def home(request):
    alumno = Alumno("Giovanni", "Ingeniería")
    curso = Curso("Fundamentos de Linux e Introducción a Django", "90 minutos")

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + " Probando",
        "python_ver": os.environ["PYTHON_VERSION"] + " más cambios",

      
        "alumno_nombre": alumno.nombre,
        "alumno_carrera": alumno.carrera, 
        "curso_nombre": curso.nombre,
        "curso_duracion": curso.duracion,
    }

    return render(request, "pages/home.html", context)
