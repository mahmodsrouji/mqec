from django.shortcuts import render
from .models import *


def masjid_quba(request):
    context = {
        'header': Header.objects.first(),
        'footer': Footer.objects.first()
    }
    return render(request, 'pages/index.html', context)

def ramadan(request):
    return render(request, 'pages/ramadan.html')

def new_muslims_correction(request):
    return render(request, 'pages/new_muslims_correction.html')

def new_muslims(request):
    return render(request, 'pages/new_muslims.html')

def about(request):
    context = {

    }
    return render(request, 'pages/about.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def donation(request):
    return render(request, 'pages/donation.html')

def non_muslims(request):
    return render(request, 'pages/non_muslims.html')

def weekly_classes(request):
    return render(request, 'pages/weekly_classes.html')

def Nikkah_ceremony(request):
    return render(request, 'pages/Nikkah_ceremony.html')
