from django.urls import path
from rapat.views import *
app_name = "rapat"

urlpatterns = [
    path('', show_pilih_pertandingan, name=''),
    path('rapat_pertandingan/<path:pertandingan>', rapat_pertandingan, name='rapat_pertandingan'),
    path('create_rapat/<path:pertandingan>', create_rapat, name='create_rapat'),
]