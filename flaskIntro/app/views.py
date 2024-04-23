# from app import conn
from flask import Flask, render_template, url_for, request, jsonify
from flask.views import MethodView
import psycopg2
from psycopg2.extras import DictCursor

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

        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM studentDetails")
            data = cur.fetchall()
            conn.commit()
        
        return jsonify(data)



    def post(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        for item in data:
            name = item.get("name")
            age = item.get("age")
            grade = item.get("grade")
            
            cur = conn.cursor()
            cur.execute("INSERT INTO studentDetails (name, age, grade) VALUES (%s,%s,%s);",(name, age, grade))
        conn.commit()
        cur.close()
        conn.close()
        return "posted successfully"

    
        


    def put(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        for item in data:
            name = item.get("name")
            age = item.get("age")
            grade = item.get("grade")
            id = item.get("id")
            
            cur = conn.cursor()
            cur.execute("UPDATE studentDetails SET name = %s, age = %s, grade = %s WHERE id = %s", (name, age, grade,id))


        conn.commit()
        cur.close()
        conn.close()
        return "updated successfully"


    def delete(self, id):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200"
        )
        
        cur = conn.cursor()
        cur.execute("DELETE FROM studentDetails WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return "deleted successfully"


product_view = learn.as_view('product_api')
views.add_url_rule('/demo1', view_func=product_view, methods=['GET', 'POST', 'PUT', 'DELETE'])






if __name__ == "__main__":
    views.run(debug=True)
