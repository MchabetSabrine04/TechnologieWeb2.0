from django.contrib import admin

from AppointementApp.models import Appointement

from .models import *


# Register your models here.
admin.site.register(User)
class AppointementStacked(admin.StackedInline):
    model=Appointement
    extra=1
class DoctorPersoClass(admin.StackedInline):
    inlines=[AppointementStacked,]
admin.site.register(Doctor,DoctorPersoClass)
admin.site.register(Patient)
admin.site.register(Speciality)
