from django.shortcuts import render

# Create your views here.
def show_rapat(request):
    return render(request, "rapat.html")

def pilih_rapat(request):
    return render(request, "pilih_rapat.html")

def mulai_pertandingan(request):
    return render(request, "mulai_pertandingan.html")

def pilih_peristiwa(request):
    return render(request, "pilih_peristiwa.html")