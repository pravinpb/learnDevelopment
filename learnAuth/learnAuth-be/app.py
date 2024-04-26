from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from psycopg2.extras import DictCursor
from functools import wraps
from flask import make_response

app = Flask(__name__)

app.config['SECRET_KEY'] = '9\xbc\xa2AC\xf7\x86\xc1{Uw\xe0'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):


        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

            conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="pravinpb",
                port="5200")
            
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM loginUsers WHERE public_id = %s;", (data['public_id'],))
                userdata = cur.fetchone()
            current_user = userdata
            
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):

    if not current_user.get('admin'):
        return jsonify({'message': 'Cannot perform that function!'}), 403

    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")
    
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM loginUsers;")
        data = cur.fetchall()

    all_users = []
    for user in data:
        public_id = user['public_id']
        name = user['name']
        all_users.append({'public_id': public_id, 'name': name, 'password': user['password'], 'admin': user['admin']})
        
    return jsonify({"users": all_users})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user,public_id):

    if not current_user.get('admin'):
        return jsonify({'message': 'Cannot perform that function!'}), 403
    
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")
    
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM loginUsers WHERE public_id = %s;", (public_id,))
        data = cur.fetchone()

        if not data:
            return jsonify({'message': 'No User Found'}), 404
    return data

@app.route('/user', methods=['POST'])
def create_user():
    
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")
    
    data = request.get_json()
    public_id = str(uuid.uuid4())
    name = data['name']
    password = data['password']
    admin = data['admin']
    
    hashed_password = generate_password_hash(password, method='scrypt')

    with conn.cursor() as cur:
        cur.execute("INSERT INTO loginUsers (public_id, name, password, admin) VALUES (%s, %s, %s, %s);",
                    (public_id, name, hashed_password, admin))
        conn.commit()

    return jsonify({'message': 'User Created'})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):

    if not current_user.get('admin'):
        return jsonify({'message': 'Cannot perform that function!'}), 403
    
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")

    with conn.cursor() as cur:
        cur.execute("UPDATE loginUsers SET admin = true WHERE public_id = %s;", (public_id,))
        conn.commit()

    return jsonify({'message': 'User Promoted'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):

    if not current_user.get('admin'):
        return jsonify({'message': 'Cannot perform that function!'}), 403
    
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")

    with conn.cursor() as cur:
        cur.execute("DELETE FROM loginUsers WHERE public_id = %s;", (public_id,))
        conn.commit()

    return jsonify({'message': 'User Deleted'})

@app.route('/login', methods=['GET'])
def login():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")

    auth = request.authorization
    name = auth.username
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM loginUsers WHERE name = %s ;", (name,))
        user = cur.fetchone()

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
     
    if not user or not check_password_hash(user['password'], auth.password):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
     
    token = jwt.encode({'public_id': user['public_id'], 'exp': datetime.utcnow() + timedelta(minutes=100)}, app.config['SECRET_KEY'])
    return jsonify('token', token)



@app.route('/todo', methods=['GET'])
@token_required
def get_all_todos(current_user):

    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")
    
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("SELECT * FROM tasklist WHERE user_id = %s;", (current_user[0],))
        data = cur.fetchall()

    return jsonify({'message': 'All todos', 'data': data})



@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todos(current_user, todo_id):
    return jsonify({'message': 'One todo'})

@app.route('/todo', methods=['POST'])
@token_required
def create_todos(current_user):

    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pravinpb",
        port="5200")
    
    data = request.get_json()
    print(data)
    print(current_user)
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute("INSERT INTO tasklist (text,complete,user_id) VALUES (%s,%s,%s);", (data['text'],data['complete'],current_user[0]))
        conn.commit()

    return jsonify({'message': 'Todo created'})

@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def update_todos(current_user, todo_id):
    return jsonify({'message': 'Todo updated'})

@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todos(current_user, todo_id):
    return jsonify({'message': 'Todo deleted'})


# @app.route('/unprotected')
# def unprotected():
#     return "This is an unprotected page"

# @app.route('/protected')
# def protected():
#     return "This is a protected page"

# @app.route('/login')
# def login():
#     auth = request.authorization
#     print("Haii", jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(seconds=300)}, app.config['SECRET_KEY']))

#     if auth and auth.password == 'password':
#         print(type(app.config['SECRET_KEY']), app.config['SECRET_KEY'])
#         token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(seconds=300)}, app.config['SECRET_KEY'])
#         return jsonify({'token': token})

#     return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True)


