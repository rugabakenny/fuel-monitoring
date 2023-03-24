from django.contrib import admin
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Company
# Register your models here.

class Accountline(admin.StackedInline):
    model = Accountuser 
    can_delete = False
    verbose_name_plural = 'Accountusers'

class CustomUseradmin(UserAdmin):
    inlines = (Accountline, )

admin.site.unregister(User)
admin.site.register(User,CustomUseradmin)
admin.site.register(Company)
admin.site.register(Station)
admin.site.register(island)
admin.site.register(Tank)
admin.site.register(Pump)
admin.site.register(Nozzle)
admin.site.register(Meters)
admin.site.register(Consumption)
admin.site.register(Technician)