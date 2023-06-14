from django.urls import path
from manage_pertandingan.views import belum_lengkap, show_list_pertandingan, lihat_peristiwa, empty_stage, akhir_musim, update_pertandingan

urlpatterns = [
    path('', belum_lengkap, name=' belum_lengkap'),
    path('list-pertandingan/', show_list_pertandingan, name='show_list_pertandingan'),
    path('lihat-peristiwa/', lihat_peristiwa, name='lihat_peristiwa'),
    path('empty-stage/', empty_stage, name='empty_stage'),
    path('akhir-musim/', akhir_musim, name='akhir_musim'),
    path('update-pertandingan/', update_pertandingan, name='update_pertandingan')
]