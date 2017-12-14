from django.shortcuts import render
from django.views.generic import TemplateView , ListView, CreateView

# Create your views here.

class LoginView(TemplateView):
	template_name = "login.html"

class AsignaturaView(TemplateView):
	#model = Asignatura
	template_name = "Asignatura.html"

class AsignaturaCrear(CreateView):
	template_name = "asignaturacrear.html"
		



