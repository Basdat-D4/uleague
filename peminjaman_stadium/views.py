from django.shortcuts import render


# Create your views here.
def show_list_pemesanan(request):
    return render(request, "list_pemesanan.html")

def show_pilih_stadium(request):
    return render(request, "pilih_stadium.html")

def show_list_waktu(request):
    return render(request, "list_waktu.html")
