from django.shortcuts import render


# Create your views here.
def show_list_pertandingan(request):
    return render(request, "list_pertandingan.html")
