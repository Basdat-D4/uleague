from django.urls import path
from pembuatan_pertandingan.views import show_home_pembuatan_pertandingan, select_stadium, select_time_stadium, tambah_pertandingan

urlpatterns = [
    path('', show_home_pembuatan_pertandingan, name='show_home_pembuatan_pertandingan'),
    path('stadium', select_stadium, name='select_stadium'),
    path('stadium/time', select_time_stadium, name='select_time_stadium'),
    path('add',tambah_pertandingan , name='tambah_pertandingan'),
    
]