from django.contrib import admin

from apps.semestral.models import Profesor, Estudiante, Asignatura, Notas

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Asignatura)
admin.site.register(Notas)