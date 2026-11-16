from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class (AbstractUser):
    pass 

class Specialty (models.Model) :
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True)
    phone=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    #specialities=models.ManyToManyField( "AccountApp.Specialty",)
    specialities=models.ManyToManyField( 
        "Specialty",
        related_name="",
        )
    


class Patient(User):
    national_id=models.CharField(max_length=8,unique=True)
    phone=models.CharField(max_length=8)
    birth_date= models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

