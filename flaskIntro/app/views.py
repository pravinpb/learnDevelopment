# from app import conn
from flask import Flask, render_template, url_for, request, jsonify,Response
from flask.views import MethodView
import psycopg2
from psycopg2.extras import DictCursor
import pandas as pd
from app import app
views = Flask(__name__)
import json


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
        df = pd.DataFrame.from_records(list(data), columns = ["id","firstname", "lastname", "email", "mobile", "grade", "gender"])
        data = df.to_dict('records')
        return Response(json.dumps(data), status=200, mimetype='application/json')



    def post(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        for item in data:
            firstname = item.get("firstname")
            lastname = item.get("lastname")
            email = item.get("email")
            mobile = item.get("mobile")
            gender = item.get("gender")
            grade = item.get("grade")
            id = item.get("id")

            cur = conn.cursor()
            cur.execute("INSERT INTO studentDetails (firstname, lastname, email, mobile, gender, grade, id) VALUES (%s,%s,%s,%s,%s,%s);",(firstname, lastname, email, mobile, grade, gender))
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
            firstname = item.get("firstname")
            lastname = item.get("lastname")
            email = item.get("email")
            mobile = item.get("mobile")
            gender = item.get("gender")
            grade = item.get("grade")
            id = item.get("id")
            
            cur = conn.cursor()
            cur.execute("UPDATE studentDetails SET name = %s, age = %s, grade = %s WHERE id = %s", (id,firstname, lastname, email, mobile, grade, gender))


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
app.add_url_rule('/student', view_func=product_view, methods=['GET', 'POST', 'PUT', 'DELETE'])

@app.route('/')
def home():
    return 'heelo'