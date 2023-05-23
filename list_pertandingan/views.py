from django.shortcuts import render


# Create your views here.
def show_list_pertandingan_penonton(request):
    return render(request, "list_pertandingan_penonton.html")

def show_list_pertandingan_manager(request):
    return render(request, "list_pertandingan_manager.html")
