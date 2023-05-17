from django.shortcuts import render
import datetime
from django.db import connection

# Create your views here.
def show_pilih_pertandingan(request):
    cursor = connection.cursor()
    cursor.execute(f'''
       SELECT
            CONCAT(tp1.Nama_Tim, ' vs ', tp2.Nama_Tim) AS "Tim Bertanding",
            s.Nama AS "Stadium",
            p.Start_DateTime || ' - ' || p.End_DateTime AS "Tanggal dan Waktu"
        FROM
            TIM_PERTANDINGAN tp1
            INNER JOIN TIM_PERTANDINGAN tp2 ON tp1.ID_Pertandingan = tp2.ID_Pertandingan
            INNER JOIN PERTANDINGAN p ON tp1.ID_Pertandingan = p.ID_Pertandingan
            INNER JOIN STADIUM s ON p.Stadium = s.ID_Stadium
        WHERE
            tp1.Nama_Tim < tp2.Nama_Tim;
    ''') # '<' to ensure theres only 1 row for each match
    pertandingan = cursor.fetchall()
    # print(pertandingan)

    pertandingan_list = []
    for p in pertandingan:
        pertandingan_list.append({
            "tim_bertanding": p[0],
            "stadium": p[1],
            "tanggal_dan_waktu": p[2]
        })

    context = {'pertandingan_list': pertandingan_list}
    return render(request, "pilih_pertandingan.html", context)

def rapat_pertandingan(request, nama_tim):
    # nama_tim = pertandingan.split(" vs ")
    context = {'nama_tim': nama_tim}
    # print(nama_tim)
    return render(request, "rapat_pertandingan.html", context)