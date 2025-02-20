from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_prayer_times, name='prayer_times'),
]
