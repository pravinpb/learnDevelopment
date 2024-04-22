# from app import conn
from flask import Flask, render_template, url_for, request, jsonify
from flask.views import MethodView
import psycopg2

views = Flask(__name__)


class learn(MethodView):
    def __init__(self):
        pass

    def get(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")

        cur = conn.cursor()
        cur.execute("SELECT * FROM studentDetails")
        print(cur.fetchall())
        conn.commit()
        cur.close()
        conn.close()



    def post(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        names = data.get("name", [])
        ages = data.get("age", [])
        grades = data.get("grade", [])
        
        values = list(zip(names, ages, grades))

        cur = conn.cursor()
        for i in range(len(values)):
            cur.execute("INSERT INTO studentDetails (name, age, grade) VALUES (%s, %s, %s)", values[i])
        conn.commit()
        cur.close()
        conn.close()

    
        # print(values)
        


    def put(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        id = data.get("id", [])
        name = data.get("name", [])

        values = list(zip(name,id))
        
        cur = conn.cursor()
        for i in range(len(values)):
            cur.execute("UPDATE studentDetails SET name = %s WHERE id = %s", values[i])
        conn.commit()
        cur.close()
        conn.close()


    def delete(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        id = data.get("id", [])
        
        cur = conn.cursor()
        for i in range(len(id)):
            cur.execute("DELETE FROM studentDetails WHERE id = %s", (id[i],))
        conn.commit()
        cur.close()
        conn.close()



product_view = learn.as_view('product_api')
views.add_url_rule('/demo1', view_func=product_view, methods=['GET', 'POST', 'PUT', 'DELETE'])






if __name__ == "__main__":
    views.run(debug=True)
