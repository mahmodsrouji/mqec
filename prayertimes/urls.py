from django.urls import path
from . import views

urlpatterns = [
    path('prayer-times/', views.get_prayer_times, name='prayer_times'),
]
