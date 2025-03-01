# prayertimes/views.py
from django.shortcuts import render

def get_prayer_times(request):
    return render(request, 'prayers/prayer_times.html')