from django.urls import path
from list_pertandingan.views import show_pertandingan
# from list_pertandingan.views import show_pertandingan_manager


urlpatterns = [
    path('', show_pertandingan, name='show_pertandingan'),
    # path('manajer/', show_pertandingan_manager, name='show_pertandingan_manager'),

]