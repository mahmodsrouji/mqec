from django.urls import path
from .views import *

urlpatterns = [
    path('', masjid_quba, name='masjid_quba'),
    path('ramadan/', ramadan, name='ramadan'),
    path('new-muslims-correction/', new_muslims_correction, name='new_muslims_correction'),
    path('new-muslims/', new_muslims, name='new_muslims'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('donation/', donation, name='donation'),
    path('non_muslims/', non_muslims, name='non_muslims'),
    path('weekly_classes/', weekly_classes, name='weekly_classes'),
    path('Nikkah_ceremony/', Nikkah_ceremony, name='Nikkah_ceremony'),
]
