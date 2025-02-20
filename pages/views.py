from django.shortcuts import render
from .models import *

def masjid_quba(request):
    context = {
        "header": Header.objects.first(),
        "navbar_items": NavbarItem.objects.all(),
        "hero": HeroSection.objects.first(),
        "about": AboutSection.objects.first(),
        "activities": Activity.objects.all(),
        "events": Event.objects.all(),
        "sermons": Sermon.objects.all(),
        "blogs": BlogPost.objects.all(),
        "team": TeamMember.objects.all(),
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, "pages/index.html", context)

def ramadan(request):
    return render(request, 'pages/ramadan.html')

def new_muslims_correction(request):
    return render(request, 'pages/new_muslims_correction.html')

def new_muslims(request):
    return render(request, 'pages/new_muslims.html')

def about(request):
    return render(request, 'pages/about.html')

def donate(request):
    return render(request, 'pages/donate.html')

