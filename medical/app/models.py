from django.db import models

# Create your models here.
# models.py

from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    description = models.TextField()
    treatment_plan = models.TextField()

    def __str__(self):
        return f"Diagnosis for {self.patient} on {self.diagnosis_date}"

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    dentist = models.ForeignKey('Dentist', on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.dentist} on {self.appointment_date} at {self.appointment_time}"

class Dentist(models.Model):
    dentist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    clinic_address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.specialization}"

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice #{self.invoice_id} for {self.patient} - {self.amount} USD"
