from django.urls import path
from pembelian_tiket.views import show_pilih_tiket
from pembelian_tiket.views import show_data_tiket
from pembelian_tiket.views import show_beli_tiket


urlpatterns = [
    path('', show_pilih_tiket, name='show_pilih_tiket'),
    path('data/', show_data_tiket, name='show_data_tiket'),
    path('beli/', show_beli_tiket, name='show_beli_tiket'),
    
]