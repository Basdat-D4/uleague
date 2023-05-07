from django.urls import path
from mengelola_tim.views import show_regis_tim, show_tim, show_daftar_pemain, show_daftar_pelatih

urlpatterns = [
    path('', show_regis_tim, name='show_regis_tim'),
    path('tim/', show_tim, name='show_tim'),
    path('daftar_pemain/', show_daftar_pemain, name='show_daftar_pemain'),
    path('daftar_pelatih/', show_daftar_pelatih, name='show_daftar_pelatih'),
]