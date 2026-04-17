from django.urls import path
from .views import home, patient_list, doctor_list, appointment_list

urlpatterns = [
    path('', home, name='home'),
    path('patients/', patient_list, name='patient_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('appointments/', appointment_list, name='appointment_list'),
]