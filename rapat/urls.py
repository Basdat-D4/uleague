from django.urls import path
from rapat.views import *
app_name = "rapat"

urlpatterns = [
    path('', show_pilih_pertandingan, name=''),
    path('rapat_pertandingan/<str:nama_tim>', rapat_pertandingan, name='rapat_pertandingan'),
]