from django.urls import path
from .views import (
    home,
    patient_list,
    doctor_list,
    appointment_list,
    add_patient,
    edit_patient,
    delete_patient,
    add_doctor,
    edit_doctor,
)

urlpatterns = [
    path("", home, name="home"),

    path("patients/", patient_list, name="patient_list"),

    path("patients/add/", add_patient, name="add_patient"),

    path(
        "patients/edit/<int:patient_id>/",
        edit_patient,
        name="edit_patient",
    ),

    path(
        "patients/delete/<int:patient_id>/",
        delete_patient,
        name="delete_patient",
    ),

    path("doctors/", doctor_list, name="doctor_list"),

    path("appointments/", appointment_list, name="appointment_list"),

    path("doctors/add/", add_doctor, name="add_doctor"),

    path("doctors/edit/<int:doctor_id>/", edit_doctor, name="edit_doctor"),
]