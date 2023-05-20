from django.db import connection
from utils.db_utils import dict_fetch_all

def get_user_role(username):
    with connection.cursor() as cursor:
        # cursor.execute('SET SEARCH_PATH TO ULEAGUE;')

        # Check Panitia
        cursor.execute(f'''
            SELECT *
            FROM PANITIA
            WHERE USERNAME='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Panitia'
        
        # Check Manajer
        cursor.execute(f'''
            SELECT *
            FROM MANAJER
            WHERE USERNAME='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Manajer'
        
        # Check Penonton
        cursor.execute(f'''
            SELECT *
            FROM PENONTON
            WHERE USERNAME='{username}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return 'Penonton'
        
    return 'none'


def check_user_availability(username, password):
    with connection.cursor() as cursor:
        cursor.execute('SET SEARCH_PATH TO ULEAGUE;')
        cursor.execute(f'''
            SELECT *
            FROM USER_SYSTEM
            WHERE USERNAME='{username}' AND PASSWORD='{password}';
        ''')
        user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:
            return True
        else:
            return False
        
