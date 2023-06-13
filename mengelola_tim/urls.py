from django.urls import path
from mengelola_tim.views import *

app_name = 'mengelola_tim'

urlpatterns = [
    path('',regis_tim, name='regis_tim'),
    path('tim/', show_tim, name='show_tim'),
    path('daftar_pemain/',daftar_pemain, name='daftar_pemain'),
    path('daftar_pelatih/', daftar_pelatih, name='daftar_pelatih'),
    path('cek_captain/<str:id>', cek_captain, name='cek_captain'),
    path('delete_tim/<str:id>/<str:role>', delete_tim, name='delete_tim'),

]