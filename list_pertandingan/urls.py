from django.urls import path
from list_pertandingan.views import show_pertandingan


urlpatterns = [
    path('', show_pertandingan, name='show_pertandingan'),
]