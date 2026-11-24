from django.db import models
from AccountApp.models import Doctor,Patient
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Appointement(models.Model):
    reason= models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status(models.TextChoices):
        PENDING = "PENDING","En attente"
        CONFIRMED=  "CONFIRMED" ,"Confirmé"
        CANCELLED = "CANCELLED" ,"Annulé"
    status= models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
   # status= models.CharField(max_length=10,choices= [("PENDING","En attente"),("CONFIRMED","Confirmé")] ,default="PENDING")
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    appointment_date=models.DateField() 
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="appointements")
    #patient=models.ForeignKey("AccountApp.Patient",on_delete=models.CASCADE,related_name="appointements")
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="appointements")
    def clean(self):
        modified_date = self._state.adding or (
            Appointement.objects.filter(
                pk=self.pk,appointment_date=self.appointment_date 
            ).exists()
        )
        if modified_date and self.appointment_date <= timezone.now().date():
            raise ValidationError("La date de l'appointment ne peut pas être dans le passé.")

    class Meta:
        ordering=["appointment_date"]
        constraints= [
            models.UniqueConstraint(
                fields= ["doctor","appointment_date"],
                name="unicite_patient-doctor-date",
                violation_error_message="ce docteur posséde un rdv avec cette date"
            )
        ]
    def __str__(self):
        return f"Rendez-vous pour le raison {self.reason} avec le docteur {self.doctor.username} le {self.appointment_date.strftime('%Y-%m-%d')}"