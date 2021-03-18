from django.contrib import admin
from .models import Projecto
# Register your models here.


#readonly_fields = ()   campos para solo lectura
class ProjectoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Projecto, ProjectoAdmin)