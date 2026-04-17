from django.shortcuts import render
from .models import Patient, Doctor


def home(request):
    return render(request, "home.html")


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "patient_list.html", {"patients": patients})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})