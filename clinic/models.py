from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ("cardiologist", "Cardiologist"),
        ("dermatologist", "Dermatologist"),
        ("pediatrican", "Pediatrican"),
        ("orthopedist", "Orthopedist"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES)
    room_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name} - {self.specialization}"
