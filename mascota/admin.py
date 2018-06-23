from django.contrib import admin

# Register your models here.
from mascota.models import Mascota, Vacuna

admin.site.register(Mascota)
admin.site.register(Vacuna)