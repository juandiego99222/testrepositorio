from django.shortcuts import render, HttpResponse

# Crea tus vistas aqui
def home(request):
    return render(request, "core/home.html")

def about(request):
     return render(request, "core/about.html")


def contacto(request):
     return render(request, "core/contacto.html")