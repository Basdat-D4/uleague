from django.urls import path
from peminjaman_stadium.views import  show_list_pemesanan, show_pilih_stadium, show_list_waktu
app_name = "peminjaman_stadium"

urlpatterns = [
    path('', show_list_pemesanan, name=' show_list_pemesanan'),
    path('pilih_stadium/', show_pilih_stadium, name='show_pilih_stadium'),
    path('list_waktu/', show_list_waktu, name='show_list_waktu'),
]