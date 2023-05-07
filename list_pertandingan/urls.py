from django.urls import path
from list_pertandingan.views import show_list_pertandingan


urlpatterns = [
    path('', show_list_pertandingan, name='show_list_pertandingan'),
    
]