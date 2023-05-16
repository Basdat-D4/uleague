from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def show_list_pemesanan(request):
    cursor = connection.cursor()
    cursor.execute(f'''
        select s.nama, p.start_datetime, p.end_datetime
        from stadium s, peminjaman p
        where s.id_stadium = p.id_stadium;
    ''')
    pemesanan = cursor.fetchall()
    # print(pemesanan)

    # convert the data into a list of dictionaries
    pemesanan_list = []
    for stadium in pemesanan:

        # change format of datetime
        start_datetime = stadium[1]
        end_datetime = stadium[2]
        formatted_start_datetime = start_datetime.strftime('%d/%m/%Y')
        formatted_end_datetime = end_datetime.strftime('%d/%m/%Y')

        pemesanan_list.append({
            'nama': stadium[0],
            'start_datetime': formatted_start_datetime,
            'end_datetime': formatted_end_datetime,
        })

    connection.close()

    context = {'pemesanan_list': pemesanan_list}
    return render(request, "list_pemesanan.html", context)

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
