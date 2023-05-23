from django.urls import path
from list_pertandingan.views import show_list_pertandingan_manager
from list_pertandingan.views import show_list_pertandingan_penonton


urlpatterns = [
    path('penonton/', show_list_pertandingan_penonton, name='show_list_pertandingan_penonton'),
    path('manager/', show_list_pertandingan_manager, name='show_list_pertandingan_manager'),
    
]