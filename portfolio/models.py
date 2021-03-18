from django.db import models

# Create your models here.
#verbose_name= cambia el nombre de lo que se ve en la pantalla, solo vista cliente
class Projecto(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link =models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion") #es automatica
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")  #es automatica
    
    class Meta:
        ordering = ["-created"]  # (-created) ordenar proyectos del mas nuevo al mas antiguo  (created)ordenar del antiguo al nuevo


    def __str__(self):
        return self.title      #nos devuelve el nombre del proyecto