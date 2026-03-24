from django.contrib import admin
from .models import Patient, Doctor, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'pesel', 'email', 'phone', 'birth_date')
    search_fields = ('first_name', 'last_name', 'pesel', 'email')
    ordering = ('first_name', 'last_name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email', 'phone', 'room_number')
    search_fields = ('first_name', 'last_name', 'email', 'room_number')
    list_filter = ('specialization',)
    ordering = ('first_name', 'last_name')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    list_filter = ('status', 'date', 'doctor')
    ordering = ('date', 'time')