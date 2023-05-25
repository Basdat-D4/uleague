from urllib import response
from django.shortcuts import redirect, render
import datetime
from django.db import connection
import uuid
from django.http import HttpResponseForbidden, HttpResponseRedirect



def regis_tim(request):
    # if request.session['role'] == "Manajer":
    #     with connection.cursor() as cursor:
    #         username_Manajer = request.COOKIES['username']
    #             #TAMPILIN PEMAIN
    #         cursor.execute ( f'''
    #             SELECT t.nama_tim, m.id_manajer
    #             FROM MANAJER m ,TIM_MANAJER t
    #             WHERE m.username = '{username_Manajer}' AND m.id_manajer = t.id_manajer;
    #         ''')
            
    #         namaTimManajer = fetch(cursor)
    #         # print (namaTimManajer)
    #         try:
    #             id_manajer = namaTimManajer[0]['id_manajer']
    #             namaTimManajer = namaTimManajer[0]["nama_tim"]
    #             if namaTimManajer:
    #                 return redirect("/mengelola_tim/tim")
    #         except Exception as e:
    #             if request.method == 'POST':
    #                 namaTimManajer = request.POST.get('team_name')
    #                 uni = request.POST.get('university_name')
                
    #                 cursor.execute(
    #                     f"""
    #                     SELECT id_manajer
    #                     FROM MANAJER
    #                     WHERE username = '{username_Manajer}'
    #                     ;
    #                     """
    #                 )
    #                 id_manajer = fetch(cursor)[0]['id_manajer']

    #                 cursor.execute(
    #                     f"""
    #                     INSERT INTO TIM (nama_tim, universitas)
    #                     VALUES ('{namaTimManajer}', '{uni}')
    #                     ;
    #                     """
    #                 )
    #                 connection.commit()
    #                 cursor.execute(
    #                     f"""
    #                     INSERT INTO TIM_MANAJER (id_manajer, nama_tim)
    #                     VALUES ('{id_manajer}', '{namaTimManajer}')
    #                     ;
    #                     """
    #                 )
    #                 connection.commit()
    #                 return redirect("/mengelola_tim/tim")
    # else:
    #     return HttpResponseForbidden("Forbidden")             
    return render(request, "regis_tim.html")

# Create your views here.
def show_tim(request):
    # dict_response = {'data_pemain':[]}
    #NGECEK MANAJER
    # username = request.COOKIES['username']
    print (request.session['role'])
    if request.session['role'] == "Manajer":      
        with connection.cursor() as cursor:
            username_Manajer = request.COOKIES['username']
            #TAMPILIN PEMAIN ---------------------------------------
            queryTim = f'''
                SELECT t.nama_tim
                FROM MANAJER m, TIM_MANAJER t
                WHERE m.username = '{username_Manajer}' AND m.id_manajer = t.id_manajer;
            '''
            cursor = connection.cursor()
            cursor.execute(queryTim)
            # namaTim = cursor.fetchone()[0]
            dataTim = fetch(cursor)[0]["nama_tim"]
            # print (dataTim)
            #TAMPILIN PEMAIN ---------------------------------------
            queryPemain = f'''
                SELECT p.id_pemain, STRING_AGG(p.nama_depan || ' ' || p.nama_belakang, ' ') AS nama, 
                p.nomor_hp, p.tgl_lahir, p.is_captain, p.posisi, p.npm, p.jenjang
                FROM PEMAIN p 
                WHERE p.nama_tim = '{dataTim}'
                GROUP BY p.id_pemain
                ORDER BY nama
            '''
            cursor = connection.cursor()
            cursor.execute(queryPemain)
            dataPemain = fetch(cursor)
            
            # for pemain in dataPemain : 
            #     dict_response['data_pemain'].append(pemain)
            
            #TAMPILIN PELATIH ---------------------------------------
            queryPelatih = f'''
                SELECT n.id, STRING_AGG(n.nama_depan || ' ' || n.nama_belakang, ' ') AS nama, 
                n.nomor_hp, n.email, n.alamat, s.spesialisasi
                FROM PELATIH p
                JOIN SPESIALISASI_PELATIH s ON p.id_pelatih = s.id_pelatih
                JOIN NON_PEMAIN n ON n.id = p.id_pelatih
                WHERE p.nama_tim = '{dataTim}'
                GROUP BY n.id, s.spesialisasi
                ORDER BY nama
            '''
            cursor = connection.cursor()
            cursor.execute(queryPelatih)
            dataPelatih = fetch(cursor)
            
            # for pelatih in dataPelatih : 
            #     dict_response['dataPelatih'].append(pelatih)
            dict_response = {
                'dataPemain': dataPemain,
                'dataPelatih': dataPelatih
            }
    else:
        return HttpResponseForbidden("Forbidden") 
    return render(request, "tim.html" ,dict_response)

def cek_captain(request, id):
    if request.session['role'] == "Manajer":      
        with connection.cursor() as cursor:
            #TAMPILIN NAMA TIM  ---------------------------------------
            cursor.execute(
                f"""
                SELECT nama_tim
                FROM PEMAIN
                WHERE id_pemain = '{id}'
                ;
                """
            )
            tim_nama = fetch(cursor)[0]["nama_tim"]
            
            cursor.execute(
                f"""
                UPDATE PEMAIN
                SET is_captain = False
                WHERE nama_tim = '{tim_nama}'
                ;
                """
            )
            connection.commit()
            cursor.execute(
                f"""
                UPDATE PEMAIN
                SET is_captain = True
                WHERE id_pemain = '{id}'
                ;
                """
            )
            connection.commit()
    else:
        return HttpResponseForbidden("Forbidden")        
    return redirect("/mengelola_tim/tim")

def delete_tim(request, id, role):
    if request.session['role'] == "Manajer":  
        with connection.cursor() as cursor:
            if role == 'pemain':
                cursor.execute(
                    f"""
                    UPDATE PEMAIN
                    SET is_captain = False, nama_tim = Null
                    WHERE id_pemain = '{id}'
                    ;
                    """
                )
            if role == 'pelatih':
                cursor.execute(
                    f"""
                    UPDATE PELATIH
                    SET nama_tim = Null
                    WHERE id_pelatih = '{id}'
                    """
                )
            connection.commit()
    else:
        return HttpResponseForbidden("Forbidden")
    return redirect("/mengelola_tim/tim") 



def daftar_pemain(request):
    if request.session['role'] == "Manajer":  
        with connection.cursor() as cursor:
            manajer_username = request.COOKIES['username']
            cursor.execute(
                f"""
                SELECT t.nama_tim
                FROM MANAJER m, TIM_MANAJER t
                WHERE m.username = '{manajer_username}' AND m.id_manajer = t.id_manajer;
                ;
                """
            )
            nama_tim = fetch(cursor)[0]["nama_tim"]
            cursor.execute(
                """
                SELECT STRING_AGG(nama_depan || ' ' || nama_belakang, ' ') AS nama, posisi, id_pemain 
                FROM PEMAIN
                WHERE nama_tim IS NULL
                GROUP BY id_pemain
                ORDER BY posisi
                ;
                """
            )
            data = fetch(cursor)
            context = {
                'data' : data
            }
            if request.method == 'POST':
                pemain = request.POST.get('pemain')
                cursor.execute(
                    f"""
                    UPDATE PEMAIN
                    SET nama_tim = '{nama_tim}'
                    WHERE id_pemain = '{pemain}'
                    ;
                    """
                )
                connection.commit()
                return redirect("/mengelola_tim/tim") 
    else:
        return HttpResponseForbidden("Forbidden")
    return render(request, "daftar_pemain.html")

def daftar_pelatih(request):
    return render(request, "daftar_pelatih.html")

def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
# ==========================================================================================

# def create_regis_tim(request):
#     if (request.session.get('username') == None):
#         return redirect('/login/')
#     if (request.session.get('nama_tim') != None):
#         return redirect('/manajer/tim/')
#     if (request.method == 'POST'):
#         nama_tim = request.POST.get('nama_tim')
#         universitas = request.POST.get('universitas')

#         response = query(f''' INSERT INTO TIM (nama_tim, universitas) VALUES ('{nama_tim}', '{universitas}') ''')
#         if (isinstance(response, Exception)):
#             context = {'message': "Nama tim sudah terdaftar"}
#             return render(request, 'registerTim.html', context)
        
#         id = query(f'''
#             SELECT id_manajer FROM MANAJER WHERE username = '{request.session.get('username')}'
#             ''')[0]['id_manajer'] 
#         response = query(f'''
#             INSERT INTO TIM_MANAJER (id_manajer, nama_tim)
#             VALUES ('{id}', '{nama_tim}')
#             ''' )
#         print(response)
#         request.session['nama_tim'] = nama_tim
#         return redirect('/manajer/kelolatim/')
#     return render(request, "regis_tim.html")


# def update_daftar_pemain(request):
#     if (request.session.get('username') == None):
#         return redirect('/authentication/login/')
#     if(request.session.get('user_role') != 'manajer'):
#         if (request.session.get('user_role') == None):
#             return redirect('/authentication/login/')
#         return redirect(f'/{request.session.get("user_role")}/')
#     list_pemain = query(f''' SELECT * FROM PEMAIN WHERE nama_tim IS NULL ''')
#     context = {'list_pemain': list_pemain}
#     if (request.method == 'POST'):
#         query(f''' UPDATE PEMAIN SET nama_tim = '{request.session.get('nama_tim')}' WHERE id_pemain = '{request.POST.get('pemain')}' ''')
#         return redirect('/manajer/kelolatim/')
#     return render(request, "daftar_pemain.html")


# def update_daftar_pelatih(request):
#     if (request.session.get('username') == None):
#         return redirect('/authentication/login/')
#     if(request.session.get('user_role') != 'manajer'):
#         if (request.session.get('user_role') == None):
#             return redirect('/authentication/login/')
#         return redirect(f'/{request.session.get("user_role")}/')
#     list_pelatih = query(f''' SELECT p.id_pelatih, nama_depan, nama_belakang, string_agg(spesialisasi, ', ') as sp
#     FROM non_pemain np
#     JOIN pelatih p ON np.id = p.id_pelatih
#     JOIN spesialisasi_pelatih sp ON p.id_pelatih = sp.id_pelatih
#     WHERE p.nama_tim IS NULL
#     GROUP BY p.id_pelatih, nama_depan, nama_belakang ''')

#     context = {'list_pelatih': list_pelatih}
#     if (request.method == 'POST'):
#         print(request.POST.get('id'))
#         response = query(f''' UPDATE PELATIH SET nama_tim = '{request.session.get('nama_tim')}' WHERE id_pelatih = '{request.POST.get('id')}' ''')
#         if (isinstance(response, Exception)):
#             context['message'] = response.args[0].split("\n")[0]
#             return render(request, 'registerPelatih.html', context)
#         else: 
#             return redirect('/manajer/kelolatim/')
#     return render(request, "daftar_pelatih.html")
    


            

    # queryManajer = f'''
    #     SELECT id_manajer
    #     FROM Manajer
    #     WHERE username = '{username_Manajer}'
    #     '''
    # cursor = connection.cursor()
    # cursor.execute(queryManajer)
    # id_manajer = cursor.fetchone()[0]
    
    
    # queryNamaTim = f'''
    #     SELECT nama_tim 
    #     FROM TIM_MANAJER 
    #     WHERE id_manajer = '{id_manajer}'
    #     '''
    # cursor = connection.cursor()
    # cursor.execute(queryNamaTim)
    # namaTim = cursor.fetchone()[0]