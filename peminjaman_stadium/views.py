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

    pemesanan_list = []
    for stadium in pemesanan:
        pemesanan_list.append({
            'nama': stadium[0],
            'start_datetime': stadium[1],
            'end_datetime': stadium[2],
        })

    connection.close()

    context = {'pemesanan_list': pemesanan_list}
    return render(request, "list_pemesanan.html", context)

def show_pilih_stadium(request):
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT NAMA, id_stadium
        FROM STADIUM
    ''')
    stadium = cursor.fetchall()
    # print(stadium)
    # response.write(stadium_list)
    connection.close()

    stadium_list = []
    for item in stadium:
        stadium_list.append({
            'nama': item[0],
            'id_stadium': item[1],
        })

    # print(stadium_list)

    context = {'stadium_list': stadium_list}
    # print(context)
    return render(request, "pilih_stadium.html", context)

def show_list_waktu(request):
    date = request.POST.get('date')
    id_stadium = request.POST.get('id_stadium')
    print(date)
    print(id_stadium)

    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT nama
        FROM stadium
        WHERE id_stadium = '{id_stadium}'
    ''')
    nama_stadium = cursor.fetchmany(1)[0][0]

    context = {
        'nama_stadium': nama_stadium
    }

    return render(request, "list_waktu.html", context)
