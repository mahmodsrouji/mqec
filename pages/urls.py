from django.urls import path
from .views import masjid_quba, ramadan, new_muslims_correction, new_muslims, about, donate

urlpatterns = [
    path('', masjid_quba, name='masjid_quba'),
    path('ramadan/', ramadan, name='ramadan'),
    path('new-muslims-correction/', new_muslims_correction, name='new_muslims_correction'),
    path('new-muslims/', new_muslims, name='new_muslims'),
    path('about/', about, name='about'),
    path('donate/', donate, name='donate'),
]
