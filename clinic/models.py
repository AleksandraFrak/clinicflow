from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



class Patient(Person):
    pesel = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.full_name()}"


class Doctor(Person):
    SPECIALIZATION_CHOICES = [
        ("cardiologist", "Cardiologist"),
        ("dermatologist", "Dermatologist"),
        ("pediatrican", "Pediatrican"),
        ("orthopedist", "Orthopedist"),
    ]

    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES)
    room_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr {self.full_name()}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("confirmed", "Confirmed"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("no_show", "No show"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor} on {self.date} at {self.time}"