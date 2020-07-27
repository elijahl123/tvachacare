from django.shortcuts import render

from .models import PatientInformation


# Create your views here.
def index(request):
    patient = PatientInformation.objects.all()
    context = {
        'object': patient
    }
    return render(request, 'homePage.html', context)


def login(request):
    return render(request, 'login.html', {})


def loginAdmin(request):
    return render(request, 'loginAdmin.html', {})
