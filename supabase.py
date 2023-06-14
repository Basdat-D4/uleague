
import psycopg2
from psycopg2 import Error
import re

try:
    connection = psycopg2.connect(user = "postgres", 
                                  password = "Q1YVHBcj7u1xvhd3", 
                                  host = "db.gxjpnwnugfupffbfnksi.supabase.co", 
                                  port = "5432", 
                                  database = "postgres")

    cursor = connection.cursor()

    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor.execute("SET SEARCH_PATH TO Uleague;")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

def execute_query(query:str):
    global cursor, connection
    query = (query.strip())
    if not (query.endswith(";")):
        query += ";"
    cursor.execute(query)
    return cursor.fetchall()

def iterate_list(lst):
    for x in lst:
        print(x)
    print()

def exec_and_print(query:str):
    iterate_list(execute_query(query))

# main
if __name__ == '__main__':
    query = '''
    select * from tim;
    '''
    exec_and_print(query.upper())