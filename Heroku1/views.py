from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 

def Inicio (request):
    return render (request, 'Heroku1/index.html')
