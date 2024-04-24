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


        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        mobile = data["mobile"]
        gender = data["gender"]
        grade = data["grade"]

        print(firstname, lastname, email, mobile)

        with conn.cursor() as cur:
            cur.execute("INSERT INTO studentDetails (firstname, lastname, email, mobile, gender, grade) VALUES (%s,%s,%s,%s,%s,%s);",
                        (firstname, lastname, email, mobile, gender, grade))
        conn.commit()
        return "posted successfully", 201\

    
        


    def put(self):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200")
        
        data = request.get_json()
        print(data)
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        mobile = data["mobile"]
        gender = data["gender"]
        grade = data["grade"]
        id = data["id"]

        print(firstname, lastname, email, mobile, id,gender, grade)

        with conn.cursor() as cur:
            cur.execute("UPDATE studentDetails SET firstname = %s, lastname = %s, email = %s, mobile = %s, gender = %s, grade = %s WHERE id = %s;",
                (firstname, lastname, email, mobile, gender, grade, id))
        conn.commit()
        return "updated successfully", 201\


    def delete(self, student_id):
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="pravinpb",
            port="5200"
        )

        with conn.cursor() as cur:
            cur.execute("DELETE FROM studentDetails WHERE id = %s;", (student_id,))
        conn.commit()
        return "deleted successfully", 200


product_view = learn.as_view('product_api')
app.add_url_rule('/student', view_func=product_view, methods=['GET', 'POST', 'PUT'])
app.add_url_rule('/student/<int:student_id>', view_func=product_view, methods=['DELETE'])


@app.route('/')
def home():
    return 'heelo'