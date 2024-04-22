import psycopg2

def conn():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")
    return conn

