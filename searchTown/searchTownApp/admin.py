from django.contrib import admin
from django.contrib import admin
from .models import Region, Departement, Town, Center

# Register your models here.

admin.site.register(Region)
admin.site.register(Departement)
admin.site.register(Town)
admin.site.register(Center)
