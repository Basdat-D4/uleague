from django.urls import path
from rapat.views import show_rapat, pilih_rapat, mulai_pertandingan, pilih_peristiwa

urlpatterns = [
    path('', show_rapat, name='show_rapat'),
    path('pilih_rapat/', pilih_rapat, name='pilih_rapat'),
    path('mulai_pertandingan/', mulai_pertandingan, name='mulai_pertandingan'),
    path('pilih_peristiwa/', pilih_peristiwa, name='pilih_peristiwa'),
]