from django.shortcuts import render
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"
    
class ContactsView(TemplateView):   
    template_name = "contacts.html"
