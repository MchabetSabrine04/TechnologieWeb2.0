from re import search

from django.contrib import admin

from AccountApp.models import Doctor
from AppointementApp.models import Appointement

# Register your models here.
@admin.action(description="Confirmer les rendez-vous")
def confirmed_appointement(model,req,queryset):
    queryset.update(status="CONFIRMED")
#admin.site.register(Appointement)

@admin.register(Appointement)
class AppointementAdminPerso(admin.ModelAdmin):
    #inlines = [DoctorPerso,]
    actions = [confirmed_appointement]
    list_display = ('reason','appointment_date','status','duration_minutes')
    list_filter = ('status','appointment_date')
    list_editable = ('status',)
    search_fields = ('reason','status')
    list_per_page = 2
    ordering = ('appointment_date',)
    fieldsets = (
        ('Description',{
            'fields':('reason','status','prescription')
        }),
        ('Date' + 'Duration',{
             'fields':('appointment_date','duration_minutes')
        }),
        ('Patient/Doctor',{
            'fields':('patient','doctor')
        }),
        ('Planification',{
            'fieleds':('created_at','update_at')
        })
    )
    readonly_fields = ('created_at','update_at')

#admin.site.register(Appointement, AppointementAdminPerso)
