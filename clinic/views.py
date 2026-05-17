from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm
from django.db.models import Q


def home(request):
    patients_count = Patient.objects.count()
    doctors_count = Doctor.objects.count()
    appointments_count = Appointment.objects.count()

    latest_appointments = Appointment.objects.order_by("date", "time")[:5]

    return render(request, "home.html", {
        "patients_count": patients_count,
        "doctors_count": doctors_count,
        "appointments_count": appointments_count,
        "latest_appointments": latest_appointments,
    })


def patient_list(request):
    query = request.GET.get("q", "")

    patients = Patient.objects.all()

    if query:
        patients = patients.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(pesel__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, "patient_list.html", {
        "patients": patients,
        "query": query,
    })


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


def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect("patient_list")

    else:
        form = PatientForm(instance=patient)

    return render(request, "edit_patient.html", {"form": form})

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        patient.delete()
        return redirect("patient_list")

    return render(request, "delete_patient.html", {"patient": patient})

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("doctor_list")

    else:
        form = DoctorForm()

    return render(request, "add_doctor.html", {"form": form})

def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            return redirect("doctor_list")

    else:
        form = DoctorForm(instance=doctor)

    return render(request, "edit_doctor.html", {"form": form})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        doctor.delete()
        return redirect("doctor_list")

    return render(request, "delete_doctor.html", {"doctor": doctor})

def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("appointment_list")

    else:
        form = AppointmentForm()

    return render(request, "add_appointment.html", {"form": form})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            return redirect("appointment_list")

    else:
        form = AppointmentForm(instance=appointment)

    return render(request, "edit_appointment.html", {"form": form})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == "POST":
        appointment.delete()
        return redirect("appointment_list")

    return render(request, "delete_appointment.html", {"appointment": appointment})