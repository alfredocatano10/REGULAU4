from django.contrib import admin
from .models import tacos, lonches, gordas


#AGREGAMOS LAS TABLAS DE LA BD EN EL SITIO WEB
modelos = tacos, lonches, gordas

admin.site.register(modelos)