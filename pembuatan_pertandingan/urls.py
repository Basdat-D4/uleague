from django.urls import path
from pembuatan_pertandingan.views import show_home_pembuatan_pertandingan, select_stadium, select_time_stadium, tambah_pertandingan
app_name = "pembuatan_pertandingan"

urlpatterns = [
    path('', show_home_pembuatan_pertandingan, name='show_home_pembuatan_pertandingan'),
    path('stadium/<path:group>', select_stadium, name='select_stadium'),
    path('time/<path:data>', select_time_stadium, name='select_time_stadium'),
    path('add/<path:data>',tambah_pertandingan , name='tambah_pertandingan'),
]