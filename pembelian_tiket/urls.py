from django.urls import path
from pembelian_tiket.views import show_pilih_tiket
from pembelian_tiket.views import show_beli_tiket
from pembelian_tiket.views import show_list_tanding
from pembelian_tiket.views import show_list_tiket

app_name = 'pembelian_tiket'

urlpatterns = [
    path('', show_pilih_tiket, name='show_pilih_tiket'),
    path('list/list_tanding/beli/', show_beli_tiket, name='show_beli_tiket'),
    path('list/', show_list_tiket, name='show_list_tiket'),
    path('list/list_tanding/', show_list_tanding, name = 'show_list_tanding')
    
]