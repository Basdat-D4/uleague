from django.shortcuts import render

# Create your views here.
def belum_lengkap(request):
    return render(request, "belum_lengkap.html")

def show_list_pertandingan(request):
    return render(request, "list_pertandingan.html")

def lihat_peristiwa(request):
    return render(request, "lihat_peristiwa.html")

def empty_stage(request):
    return render(request, "empty_stage.html")

def akhir_musim(request):
    return render(request, "akhir_musim.html")

def update_pertandingan(request):
    return render(request, "update_pertandingan.html")
