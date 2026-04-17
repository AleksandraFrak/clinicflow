from django.shortcuts import render
from .models import Patient

def home(request):
    return render(request, "home.html")


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "patient_list.html", {"patients": patients})