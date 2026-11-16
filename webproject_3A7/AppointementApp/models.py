from django.db import models
from AccountApp.models import Doctor

# Create your models here.

class Appointement(models.Model):
    reason=models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status(models.TextChoices):
        PENDING="PENDING","En attente"
        CONFIRMED="CONFIRMED" ,"Confirmé"
        CANCELLED="CANCELED" , "Annulé"
    status= models.CharField(max_length=10,choices=Status.choices,default="PENDING")
#status= models.CharField(max_length=10,choices=[("PENDING","En attente"),("CONFIRMED" ,"Confirmé")],default="PENDING")
duration_minutes=models.PositiveBigIntegerField(default)
created_at=models.DateTimeField(auto_now_add=True)
update_at=models.DateTimeField(auto_now=True)
appointement_date=models.DateField()
doctor=models.ForeignKey(Doctor,on_delete==models.CASCADE,related_name="appointements")
patient=models.ForeignKey("AccountApp.Patient",on_delete=models.CASCADE,related_name="Appointements")
class Meta:
    constraints= [
        models.UniqueConstraint(
            fields=["doctor","appointement_date"],
            name="unicite_patient-doctor-date",
            violation_error_message="ce docteur posséde un rdv avec cette date"
        )
    ]