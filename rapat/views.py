from django.shortcuts import render

# Create your views here.
def show_rapat(request):
    return render(request, "rapat.html")