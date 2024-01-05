from django.shortcuts import render
from rest_framework import generics
from .models import Patient, Diagnosis, Appointment, Dentist, Invoice
from .serializers import PatientSerializer, DiagnosisSerializer,UserSerializer ,AppointmentSerializer, DentistSerializer, InvoiceSerializer
from django.contrib.auth.models import User

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DiagnosisListCreateView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DentistListCreateView(generics.ListCreateAPIView):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer