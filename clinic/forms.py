from django import forms
from .models import Patient, Doctor, Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "first_name",
            "last_name",
            "pesel",
            "birth_date",
            "email",
            "phone",
        ]

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "specialization",
            "room_number",
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "patient",
            "doctor",
            "date",
            "time",
            "status",
            "notes",
        ]