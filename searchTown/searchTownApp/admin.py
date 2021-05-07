from django.contrib import admin
from django.contrib import admin
from .models import CodesPostaux, Region, Departement, Town

# Register your models here.

admin.site.register(CodesPostaux)
admin.site.register(Region)
admin.site.register(Departement)
admin.site.register(Town)