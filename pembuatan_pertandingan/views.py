from django.shortcuts import render
from django.shortcuts import redirect
from supabase import *
import requests
import uuid
# Create your views here.
def show_home_pembuatan_pertandingan(request):
    # data = execute_query(f'''
    #     SELECT TIM1.id_pertandingan, CONCAT(TIM1.nama_tim, ' VS ', TIM2.nama_tim)
    #     FROM TIM_PERTANDINGAN TIM1
    #     JOIN PERTANDINGAN P ON TIM1.id_pertandingan = P.id_pertandingan
    #     JOIN TIM_PERTANDINGAN TIM2 ON TIM2.id_pertandingan = TIM1.id_pertandingan
    #     WHERE TIM2.nama_tim != TIM1.nama_tim
    #     GROUP BY TIM1.id_pertandingan;
    # ''')

    data = execute_query(f'''
            SELECT DISTINCT TIM3.id_pertandingan, CONCAT(temp2.tim_1, ' VS ', TIM3.nama_tim)
            FROM tim_pertandingan TIM3 
            natural join (
                SELECT TIM1.id_pertandingan, TIM1.nama_tim as tim_1
                FROM PERTANDINGAN P
                NATURAL JOIN tim_pertandingan TIM1
            ) as TEMP2
            where TIM3.nama_tim != tim_1
    ''')

    ST = ' '
    ST = ST.join(map(str, data))
    result = ST.split(") (")
    DATA =[]
    # print(ST)
    for item in result:   
        items = item.split(", ")
        byte = [
            items[0].replace("UUID('", "").replace(")","").replace("'", ""), 
            items[1].replace("'", "").replace(")","")
        ]
        print(byte)
        DATA.append(byte)
    #Struktur :
    # [
    #   [[GRUP A], [GRUP B]]
    # ]
    REMOVE_DATA = []
    DATA_A = []
    DATA_B = [] 
    for i in DATA:
        # print(i[1])
        if i[0][0:2] == "0a":
            if i[0] in REMOVE_DATA:
                continue
            else:
                REMOVE_DATA.append(i[0])
                DATA_A.append(i)
        else:
            if i[0] in REMOVE_DATA:
                continue
            else:
                REMOVE_DATA.append(i[0])
                DATA_B.append(i)

    return render(request, "home_pembuatan_pertandingan.html", {
        'first_data': DATA_A,
        'second_data': DATA_B,
        'first_data': DATA_A,
        'second_data': DATA_B,
    })

def select_stadium(request, group):

    fetch_data = execute_query("SELECT nama FROM STADIUM;")
    fetch_data = list(fetch_data)
    ST = ' '
    ST = ST.join(map(str, fetch_data))
    result = ST.split(") (")
    DATA =[]
    for item in result:
        newItem = item.replace("',", "").replace("'", "").replace("(", "").replace(")", "")
        DATA.append(newItem)


    if request.method == "POST":
        stadium = request.POST.get("stadium")
        tanggal = request.POST.get('tanggal')

        # request.session['stadium'] =  str(title_task)
        # print(str(request.session.get('stadium')))
        # requests.session.modified = True

        context = {
            'group' : group,
            'stadium' : stadium,
            'tanggal' : tanggal,
        }
        return redirect('pembuatan_pertandingan:select_time_stadium', str(context))
    
    return render(request, "stadium_and_date.html", {
        "daftar_stadium": DATA,
        "context": {
            'group' : group
        }
        })

def select_time_stadium(request, data):
    data = eval(data)
    print("INI DATA DARI SELECT TIMER STADIUM")
    print(str(data))

    
    # GET DATA STADIUM YANG DAPAT DIGUNAKAN
    # DATA_FETCH = execute_query(f'''
        
    # ''')
    
    return render(request, "select_time.html", {
        'stadium' : data['stadium'],
        'result' : [
            {'stadium' : data['stadium'],
            'waktu' : '07.00 - 09.00',  
            'status': False
             },
            {'stadium' : data['stadium'],
            'waktu' : '11.00 - 13.00',
            'status': True
             },
        ]
        
    })


def tambah_pertandingan(request, data):
    print(eval(data))
    #GET DATA WASIT
    fetch_data_wasit = execute_query("""
        SELECT N.ID, N.Nama_depan, N.nama_belakang 
        FROM WASIT W, NON_PEMAIN N 
        WHERE N.ID = W.ID_wasit;
        """)
    fetch_data_wasit = list(fetch_data_wasit)
    result_data_wasit = []
    for items in fetch_data_wasit:
        temp = []
        counter = 0
        for a in items:
            if counter == 0:
                temp.append(str(a))
            elif counter == 1:
                temp.append(str(a))
            else:
                temp[1] = temp[1] +" "+ str(a)
            counter += 1
        result_data_wasit.append(temp) 

    #GET DATA DARI TIM YANG SUDAH MENDAFTAR LAPANGAN
    fetch_data_tim = execute_query("""
        SELECT DISTINCT tim.nama_tim
        FROM TIM
        JOIN tim_manajer MAN on MAN.nama_tim = TIM.nama_tim
        JOIN peminjaman PEM ON PEM.id_manajer = MAN.id_manajer
        WHERE '2023-05-06' BETWEEN PEM.start_datetime and PEM.end_datetime
        """)

    fetch_data_tim = list(fetch_data_tim)
    print(fetch_data_tim)
    result_data_tim =[]
    for items in fetch_data_tim:
        temp = str(items).replace(",", "").replace("'","").replace("(", "").replace(")","")
        result_data_tim.append(temp)
    #TODO: LOGIC INSERT DATA
    uudi_pertandingan = uuid.uuid4()
    uudi_pertandingan = str(uudi_pertandingan)
    print(uudi_pertandingan)
    print("0a"+uudi_pertandingan[2:])


    if request.method == "POST":
        WASIT_UTAMA = request.POST.get("wasit-utama")
        WASIT_PEMBANTU_1 = request.POST.get("wasit-pembantu-1")
        WASIT_PEMBANTU_2 = request.POST.get("wasit-pembantu-2")
        WASIT_CADANGAN = request.POST.get("wasit-cadangan")

        TIM_1 = request.POST.get("tim-1")
        TIM_2 = request.POST.get("tim-2")
        
        # uudi_pertandingan = uuid.uuid4()
        uudi_pertandingan = uuid.uuid4()
        uudi_pertandingan = str(uudi_pertandingan)
        uudi_pertandingan = '0b' + uudi_pertandingan[2:]

        # execute_query('''
        #     INSERT INTO PERTANDINGAN (ID_PERTANDINGAN, Start_DateTime, End_Datetime, Stadium) VALUES ('{uudi_pertandingan}', '2023-05-01 8:00:00', '2023-05-01 10:00:00', 'e54965f3-f636-472a-a089-74ff111f8c1b');
        # ''')

        # INSERT TIM PERTANDINGAN
        # execute_query('''
        # ''')

        # INSERT WASIT BERTUGAS PERTANDINGAN
        # execute_query('''
        # ''')
        
    return render(request, "fix_match.html", 
                  {'daftar_wasit': result_data_wasit,
                   'daftar_tim': result_data_tim
                   })