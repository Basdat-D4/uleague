from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def show_list_pemesanan(request):
    return render(request, "list_pemesanan.html")

def show_pilih_stadium(request):
    # response = HttpResponse()

    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT NAMA
        FROM STADIUM
    ''')
    stadium_list = cursor.fetchall()
    # response.write(stadium_list)
    connection.close()

    names_list = []
    for stadium in stadium_list:
        names_list.append(stadium[0])

    context = {'stadium_names': names_list}
    print(context)
    return render(request, "pilih_stadium.html", context)

def show_list_waktu(request):
    return render(request, "list_waktu.html")
