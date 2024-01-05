from django.contrib import admin
from .models import Patient, Diagnosis, Appointment, Dentist, Invoice

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'email', 'address')
    search_fields = ('first_name', 'last_name', 'contact_number', 'email')

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('diagnosis_id', 'patient', 'diagnosis_date', 'description', 'treatment_plan')
    search_fields = ('patient__first_name', 'patient__last_name', 'description')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'patient', 'appointment_date', 'appointment_time', 'dentist', 'notes')
    search_fields = ('patient__first_name', 'patient__last_name', 'dentist__first_name', 'dentist__last_name', 'notes')

@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ('dentist_id', 'first_name', 'last_name', 'specialization', 'contact_number', 'email', 'clinic_address')
    search_fields = ('first_name', 'last_name', 'specialization', 'contact_number', 'email')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'patient', 'appointment', 'invoice_date', 'amount')
    search_fields = ('patient__first_name', 'patient__last_name', 'amount')
