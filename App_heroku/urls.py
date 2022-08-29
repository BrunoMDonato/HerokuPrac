
from django.contrib import admin
from django.urls import path
from Heroku1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', Inicio, name='Inicio')
]
