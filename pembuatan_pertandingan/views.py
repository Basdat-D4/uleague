from django.shortcuts import render

# Create your views here.
def show_home_pembuatan_pertandingan(request):
    return render(request, "home_pembuatan_pertandingan.html")

def buat_pertandingan_select_stadium(request):
    return render(request, "stadium_and_date.html")

def select_waktu_pertandingan(request):
    return render(request, "select_time.html")

def final_buat_pertandingan(request):
    return render(request, "fix_match.html")