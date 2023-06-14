from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from utils.db_utils import dict_fetch_all
from django.views.decorators.csrf import csrf_exempt
from utils.users import get_user_role
from django.contrib import messages
from utils.users import *


# Login
def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
        response = HttpResponse()
        username = request.POST['username']
        password = request.POST['password']
        with connection.cursor() as cursor:
            cursor.execute(f'''
                SELECT *
                FROM USER_SYSTEM
                WHERE username='{username}' AND password='{password}';
            ''')
            user_list = dict_fetch_all(cursor)

        if len(user_list) != 0:
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            response.status_code = 200
            return response
        else:
            response.status_code = 404
            print("login failed")
            response.delete_cookie('username')
            response.delete_cookie('password')
            return response
    return HttpResponse(status=404)


# Logout
def logout_user(request):
    response = HttpResponse(status=200)
    response.delete_cookie('username')
    response.delete_cookie('password')
    print("logout")
    return HttpResponseRedirect("/login/")

# Register
def register_user(request):
    return render(request, 'registration.html', {})

@csrf_exempt
def register_panitia(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        id_panitia = request.POST.get('id_panitia')
        jabatan = request.POST.get('jabatan')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        nomor_hp = request.POST.get('nomor_hp')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')

        if (id_panitia != "" and jabatan != "" and username != "" and password != ""):
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f'''
                        INSERT INTO USER_SYSTEM VALUES ('{username}', '{password}');
                        INSERT INTO NON_PEMAIN VALUES ('{id_panitia}', '{nama_depan}', '{nama_belakang}', '{nomor_hp}', '{email}', '{alamat}');
                        INSERT INTO PANITIA VALUES ('{id_panitia}', '{jabatan}', '{username}');
                    ''')

                    response = HttpResponse()
                    response.set_cookie('username', username)
                    response.set_cookie('password', password)
                    response.status_code = 200

                    show_dashboard(request)
                    return response
                except Exception as e:
                    print(e)
                    res = str(e).split('\n')[0]
                    messages.error(request, res)
    
        else:
            messages.error(request, "Please fill all the fields")
    return render(request, 'reg_panitia.html', {})


def register_manajer(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        id_manajer = request.POST.get('id_manajer')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        nomor_hp = request.POST.get('nomor_hp')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')

        if (id_manajer != "" and username != "" and password != ""):
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f'''
                        INSERT INTO USER_SYSTEM VALUES ('{username}', '{password}');
                        INSERT INTO NON_PEMAIN VALUES ('{id_manajer}', '{nama_depan}', '{nama_belakang}', '{nomor_hp}', '{email}', '{alamat}');
                        INSERT INTO MANAJER VALUES ('{id_manajer}', '{username}');
                    ''')

                    response = HttpResponse()
                    response.set_cookie('username', username)
                    response.set_cookie('password', password)
                    response.status_code = 200

                    show_dashboard(request)
                    return response
                except Exception as e:
                    print(e)
                    res = str(e).split('\n')[0]
                    messages.error(request, res)
        else:
            messages.error(request, "Please fill all the fields")

    return render(request, 'reg_manajer.html', {})


def register_penonton(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        id_penonton = request.POST.get('id_penonton')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        nomor_hp = request.POST.get('nomor_hp')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')

        if (id_penonton != "" and username != "" and password != ""):
            with connection.cursor() as cursor:
                try:
                    cursor.execute(f'''
                        INSERT INTO USER_SYSTEM VALUES ('{username}', '{password}');
                        INSERT INTO NON_PEMAIN VALUES ('{id_penonton}', '{nama_depan}', '{nama_belakang}', '{nomor_hp}', '{email}', '{alamat}');
                        INSERT INTO PENONTON VALUES ('{id_penonton}', '{username}');
                    ''')

                    response = HttpResponse()
                    response.set_cookie('username', username)
                    response.set_cookie('password', password)
                    response.status_code = 200

                    show_dashboard(request)
                    return response
                
                except Exception as e:
                    print(e)
                    res = str(e).split('\n')[0]
                    messages.error(request, res)
        else:   
            messages.error(request, "Please fill all the fields")
    return render(request, 'reg_penonton.html', {})

def show_dashboard(request):
    username = request.COOKIES['username']

    role = get_user_role(username)
    print("role: " + role)
    context = {
        'user': {
            'role': f'{role}',
        }
    }

    with connection.cursor() as cursor:
        if role == 'Panitia':
            cursor.execute(f'''
                SELECT * FROM PANITIA WHERE username='{username}';
            ''')
            data = dict_fetch_all(cursor)
            context['data'] = data[0]
            print(data[0])
            return render(request, 'dashboard_panitia.html', context)
        elif role == 'Manajer':
            cursor.execute(f'''
                SELECT * FROM MANAJER WHERE username='{username}';
            ''')
            data = dict_fetch_all(cursor)
            context['data'] = data[0]
            print(data[0])
            return render(request, 'dashboard_manajer.html', context)
        elif role == 'Penonton':
            cursor.execute(f'''
                SELECT * FROM PENONTON WHERE username='{username}';
            ''')
            data = dict_fetch_all(cursor)
            context['data'] = data[0]
            print(data[0])
            return render(request, 'dashboard_penonton.html', context)
            

    return render(request, 'dashboard_panitia.html', context)