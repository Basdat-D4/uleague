from django.shortcuts import render
from django.db import connection

# Create your views here.
def show_history_rapat(request):
    cursor = connection.cursor()
    cursor.execute(f'''
       SELECT 
            tp1.Nama_Tim || ' vs ' || tp2.Nama_Tim AS "Tim Bertanding",
            MAX(CONCAT (np.nama_depan, ' ', np.nama_belakang)) AS "Nama Panitia",
            (s.Nama) AS "Stadium",
            r.DateTime  AS "Tanggal dan Waktu"
        FROM
            NON_PEMAIN np, TIM_PERTANDINGAN tp1
            INNER JOIN TIM_PERTANDINGAN tp2 ON tp1.ID_Pertandingan = tp2.ID_Pertandingan 
            INNER JOIN PERTANDINGAN p ON tp1.ID_Pertandingan = p.ID_Pertandingan
            INNER JOIN STADIUM s ON p.Stadium = s.ID_Stadium
            INNER JOIN rapat r ON r.ID_pertandingan = tp1.ID_pertandingan
            INNER JOIN non_pemain np1 ON r.perwakilan_panitia = np1.id 
        WHERE
            tp1.Nama_Tim > tp2.Nama_Tim AND np.id > r.perwakilan_panitia
        GROUP BY
        tp1.ID_Pertandingan, tp1.Nama_Tim, tp2.Nama_Tim, s.ID_Stadium, r.DateTime;
                
''') 
    history = cursor.fetchall()
    cursor.close()

    history_list = []
    for i in range(len(history)):
        tim_bertanding = history[i][0]
        nama_panitia = history[i][1]
        stadium =  history[i][2]
        tanggal_dan_waktu =  history[i][3]
        history_list.append({'tim_bertanding' : tim_bertanding, 'nama_panitia' : nama_panitia, 'stadium' :  stadium, 'tanggal_dan_waktu' : tanggal_dan_waktu})

    context = {'history_list': history_list}
    return render(request, "history_rapat.html", context)


