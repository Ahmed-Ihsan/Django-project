from django.shortcuts import render
import requests

def patients_list(request):
    api_url = 'http://localhost:8000/api/patients/'  # Update with your API URL
    response = requests.get(api_url)
    patients = response.json()
    return render(request, 'patients_list.html', {'patients': patients})

def diagnoses_list(request):
    api_url = 'http://localhost:8000/api/diagnoses/'  # Update with your API URL
    response = requests.get(api_url)
    diagnoses = response.json()
    return render(request, 'diagnoses_list.html', {'diagnoses': diagnoses})

def appointments_list(request):
    api_url = 'http://localhost:8000/api/appointments/'  # Update with your API URL
    response = requests.get(api_url)
    appointments = response.json()
    return render(request, 'appointments_list.html', {'appointments': appointments})

def dentists_list(request):
    api_url = 'http://localhost:8000/api/dentists/'  # Update with your API URL
    response = requests.get(api_url)
    dentists = response.json()
    return render(request, 'dentists_list.html', {'dentists': dentists})

def invoices_list(request):
    api_url = 'http://localhost:8000/api/invoices/'  # Update with your API URL
    response = requests.get(api_url)
    invoices = response.json()
    return render(request, 'invoices_list.html', {'invoices': invoices})
