from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from .forms import PatientForm


def home(request):
    return render(request, "home.html")


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "patient_list.html", {"patients": patients})


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, "appointment_list.html", {"appointments": appointments})


def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("patient_list")

    else:
        form = PatientForm()

    return render(request, "add_patient.html", {"form": form})