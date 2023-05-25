from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect, render

# Create your views here.
def show_pertandingan(request):
    # role = request.COOKIES.get('role')
    # if role == None:
    #     return redirect('authentication:login_user')
    # if role not in ['Penonton', 'Manajer']:
    #     return redirect('authentication:show_dashboard')
    
    cursor = connection.cursor()
    cursor.execute(f'''
       SELECT
            CONCAT(tp1.Nama_Tim, ' vs ', tp2.Nama_Tim) AS "Tim Bertanding",
            s.Nama AS "Stadium",
            CONCAT(p.Start_DateTime, ' - ' , p.End_DateTime) AS "Tanggal dan Waktu"
        FROM
            TIM_PERTANDINGAN tp1
            INNER JOIN TIM_PERTANDINGAN tp2 ON tp1.ID_Pertandingan = tp2.ID_Pertandingan
            INNER JOIN PERTANDINGAN p ON tp1.ID_Pertandingan = p.ID_Pertandingan
            INNER JOIN STADIUM s ON p.Stadium = s.ID_Stadium
        WHERE
            tp1.Nama_Tim < tp2.Nama_Tim

        GROUP BY "Tim Bertanding", "Stadium", "Tanggal dan Waktu"
            ;
    ''') 
    pertandingan = cursor.fetchall()
    cursor.close()
    # print(pertandingan)
    # print(rapat_util)

    pertandingan_list = []
    for i in range(len(pertandingan)):
        tim_bertanding = pertandingan[i][0]
        stadium = pertandingan[i][1]
        tanggal_dan_waktu = pertandingan[i][2]
        pertandingan_list.append({
            'tim_bertanding': tim_bertanding,
            'stadium': stadium,
            'tanggal_dan_waktu': tanggal_dan_waktu
        })

    context = {'pertandingan_list': pertandingan_list}
    return render(request, "list_pertandingan.html", context)





