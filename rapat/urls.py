from django.urls import path
from rapat.views import show_rapat

urlpatterns = [
    path('', show_rapat, name='show_rapat'),
]