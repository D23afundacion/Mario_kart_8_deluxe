from django.contrib import admin
from .models import Usuarios, Copas, Pistas, Equipamientos, Records, Adquiridos

admin.site.register(Usuarios)
admin.site.register(Copas)
admin.site.register(Pistas)
admin.site.register(Equipamientos)
admin.site.register(Records)
admin.site.register(Adquiridos)