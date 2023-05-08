from django.shortcuts import render

# Create your views here.
def show_regis_tim(request):
    return render(request, "regis_tim.html")

def show_tim(request):
    return render(request, "tim.html")

def show_daftar_pemain(request):
    return render(request, "daftar_pemain.html")

def show_daftar_pelatih(request):
    return render(request, "daftar_pelatih.html")