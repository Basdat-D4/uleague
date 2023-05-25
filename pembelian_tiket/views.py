import random
import string
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db import connection

# def generate_receipt(request):
#     characters = string.ascii_letters + string.digits
#     receipt = ''.join(random.choice(characters) for i in range(50))
    
#     cursor = connection.cursor()
#     cursor.execute("SELECT COUNT(*) FROM PEMBELIAN_TIKET WHERE nomor_receipt = %s", [receipt])
#     count = cursor.fetchone()[0]
#     if count > 0:
#         return generate_receipt()
#     return receipt

def show_beli_tiket(request):
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT jenis_tiket, jenis_pembayaran
        FROM pembelian_tiket
    ''')
    payment = cursor.fetchall()
    tiket_list = []
    for item in payment:
        tiket_list.append({
            'jenis_tiket': item[0],
            'jenis_pembayaran': item[1],
        })
    context = {'tiket_list': tiket_list}
    if request.method == 'POST':
        request.session['jenis_tiket'] = request.POST.get('selected_dt')
        request.session['jenis_pembayaran'] = request.POST.get('jenis_pembayaran')
        return redirect('pembelian_tiket:show_pilih_tiket')
    return render(request, "beli_tiket.html", context)

# def show_gene_tiket(request):
#     # username = request.session["username"]
#     username = "upin"
#     if request.method == 'get':
#         jenis_tiket = request.POST.get('jenis_tiket')
#         jenis_pembayaran = request.POST.get('jenis_pembayaran')
#         nomor_receipt = generate_receipt()
#         print(jenis_tiket)
#         print(jenis_pembayaran)
        
#         id_penonton = (f'''SELECT DISTINCT P.id_penonton as id
#             FROM PENONTON P WHERE user_system.username = '{username}';
#             ''')
    
#         for penonton in id_penonton:
#             membeli_tiket = (
#                 f"""INSERT INTO PEMBELIAN_TIKET (nomor_receipt, id_penonton, jenis_tiket, jenis_pembayaran, id_pertandingan) 
#                 VALUES ('{nomor_receipt}', '{penonton.id}', '{jenis_tiket}', '{jenis_pembayaran}', '{id_pertandingan}'; """)
            
#         print(membeli_tiket, "oko")
#         return JsonResponse({'success': 'true', 'message': 'Berhasil membeli tiket!'}, status=200)
#     context = {
#     'username' : username,
#     'id_pertandingan': id,
#     }

#     return render(request, 'pilih_tiket.html', context)


def show_pilih_tiket(request):
    # if request.session['role'] == 'penonton':
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT NAMA, id_stadium
        FROM STADIUM
    ''')
    stadium = cursor.fetchall()
    stadium_list = []
    for item in stadium:
        stadium_list.append({
            'nama': item[0],
            'id_stadium': item[1],
        })
    context = {'stadium_list': stadium_list}
    if request.method == 'POST':
        request.session['selected_dt'] = request.POST.get('selected_dt')
        request.session['id_stadium'] = request.POST.get('id_stadium')
        return redirect('pembelian_tiket:show_list_tiket')
    return render(request, "pilih_tiket.html", context)

def show_list_tanding(request):    
    selected_dt = request.session['selected_dt']
    id_stadium = request.session['id_stadium']
    # print("vvvv",selected_dt)

    # print("vsvs",id_stadium)
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT tp1.Nama_Tim as "Tim 1", tp2.Nama_Tim as "Tim 2"
        FROM TIM_PERTANDINGAN tp1
        INNER JOIN TIM_PERTANDINGAN tp2 ON tp1.ID_Pertandingan = tp2.ID_Pertandingan
        INNER JOIN PERTANDINGAN p ON tp1.ID_Pertandingan = p.ID_Pertandingan
        INNER JOIN STADIUM s ON p.Stadium = s.ID_Stadium

        WHERE DATE(p.start_datetime) = %s AND tp1.Nama_Tim < tp2.Nama_Tim
        GROUP BY "Tim 1", "Tim 2";
        ''', [selected_dt])
    
    # print("vddvvv",selected_dt)

    tiket = cursor.fetchall()

    pertandingan_list = []
    for i in range(len(tiket)):
        tim_A = tiket[i][0]
        tim_B = tiket[i][1]
        pertandingan_list.append({
            'tim_A': tim_A,
            'tim_B': tim_B,
        })
    # print("ba", pertandingan_list)

    context = {'pertandingan_list': pertandingan_list}

    return render(request, "list_tanding.html", context)

def show_list_tiket(request):
    # if request.session['role'] == 'penonton':
    selected_dt = request.session['selected_dt']
    id_stadium = request.session['id_stadium']
    cursor = connection.cursor()
    cursor.execute("""
            SELECT s.nama
            FROM pertandingan p
            INNER JOIN stadium s ON p.stadium = s.id_stadium
            WHERE DATE(p.start_datetime) = %s AND s.nama = %s
        """, [selected_dt, id_stadium])
    if id_stadium is not None:
        id_stadium = id_stadium
    else:
        id_stadium = "stadium"
        return redirect('show_pilih_tiket')       
    cursor = connection.cursor()
    cursor.execute("""
        SELECT TO_CHAR(p.start_datetime AT TIME ZONE 'GMT7', 'HH24:MI' ) || ' - ' || 
        TO_CHAR(p.end_datetime AT TIME ZONE 'GMT7', 'HH24:MI') as "List Waktu"
        FROM pertandingan p
        INNER JOIN stadium s ON p.stadium = s.id_stadium
        INNER JOIN tim_pertandingan tp ON tp.id_pertandingan = p.id_pertandingan
        WHERE s.nama = %s; 
        """, [id_stadium])
    
    thetime = cursor.fetchone()
    
    # print ("mm", thetime)
    list_time = []
    if thetime is not None:
        for i in range (len(thetime)):
            list_time.append({ 'list_waktu': thetime[i]})
    else:
        print("tidak ada jadwal.")
    nama_stadium = id_stadium
    context = {'nama_stadium': nama_stadium, 'list_time': list_time}
    return render(request, 'list_tiket.html', context)






