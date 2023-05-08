from django.urls import path
from pembuatan_pertandingan.views import show_home_pembuatan_pertandingan, buat_pertandingan_select_stadium, select_waktu_pertandingan, final_buat_pertandingan

urlpatterns = [
    path('', show_home_pembuatan_pertandingan, name='show_home_pembuatan_pertandingan'),
    path('buat-pertandingan', buat_pertandingan_select_stadium, name='buat_pertandingan_select_stadium'),
    path('buat-pertandingan/pilih-waktu-stadium', select_waktu_pertandingan, name='select_waktu_pertandingan'),
    path('buat-pertandingan/finalisasi',final_buat_pertandingan , name='final_buat_pertandingan'),
]