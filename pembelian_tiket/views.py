from django.shortcuts import render

# Create your views here.
def show_pilih_tiket(request):
    return render(request, "pilih_tiket.html")

def show_data_tiket(request):
    return render(request, "data_tiket.html")

def show_beli_tiket(request):
    return render(request, "beli_tiket.html")
