from django.urls import path
from .views import PatientListCreateView, DiagnosisListCreateView, AppointmentListCreateView, DentistListCreateView,UserCreateView ,InvoiceListCreateView

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('diagnoses/', DiagnosisListCreateView.as_view(), name='diagnosis-list-create'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('dentists/', DentistListCreateView.as_view(), name='dentist-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]