
from django.urls import path
from .views import patients_list, diagnoses_list, appointments_list, dentists_list, invoices_list

urlpatterns = [
    path('patients/', patients_list, name='patients_list'),
    path('diagnoses/', diagnoses_list, name='diagnoses_list'),
    path('appointments/', appointments_list, name='appointments_list'),
    path('dentists/', dentists_list, name='dentists_list'),
    path('invoices/', invoices_list, name='invoices_list'),
]