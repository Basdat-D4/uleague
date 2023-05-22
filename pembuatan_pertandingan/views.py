from django.shortcuts import render
from django.shortcuts import redirect
from supabase import *
import requests
import uuid

# Create your views here.
def show_home_pembuatan_pertandingan(request):

    return render(request, "home_pembuatan_pertandingan.html")

def select_stadium(request):
    # #TODO:
    myuuid = uuid.uuid4()
    myuuid = str(myuuid)
    newuuid = "0A" + myuuid[2:len(myuuid)]
    print('Your UUID is: ' + str(myuuid))
    print('Your UUID NEW: ' + newuuid)


    fetch_data = execute_query("SELECT universitas FROM TIM;")
    fetch_data = list(fetch_data)
    ST = ' '
    ST = ST.join(map(str, fetch_data))
    result = ST.split(") (")
    DATA =[]
    for item in result:
        newItem = item.replace("',", "").replace("'", "").replace("(", "").replace(")", "")
        DATA.append(newItem)
    print(DATA)

    if 'stadium' in request.session:
            print("remove")
            request.session.clear()
    
    if request.method == "POST":
        title_task = request.POST.get("stadium")
        description_task = request.POST.get('tanggal')

        request.session['stadium'] =  str(title_task)
        print(str(request.session.get('stadium')))
  
        requests.session.modified = True
        return redirect(
            'pembuatan_pertandingan:select_time_stadium')
    
    return render(request, "stadium_and_date.html", {"daftar_stadium": DATA})

def select_time_stadium(request):

    return render(request, "select_time.html", 
                  context={
                       'stadium': str(request.session.get('stadium')),
                       })


def tambah_pertandingan(request):
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
        SELECT nama_tim 
        FROM TIM;
        """)
    fetch_data_tim = list(fetch_data_tim)
    result_data_tim =[]
    for items in fetch_data_tim:
        temp = str(items).replace(",", "").replace("'","").replace("(", "").replace(")","")
        result_data_tim.append(temp)
    #TODO
    return render(request, "fix_match.html", 
                  {'daftar_wasit': result_data_wasit,
                   'daftar_tim': result_data_tim
                   })