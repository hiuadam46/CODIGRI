from flask import render_template
from flask import Flask, jsonify
import coreapi
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request
import jwt
from datetime import datetime, timedelta

secret_key1 = "TSTMY"
secret_key2 = "TSTKRI"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50))

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_room = db.Column(db.Integer)
    message = db.Column(db.String(250))

@app.route("/")
def home():
    init()
    with app.app_context():
        return render_template("home.html")

@app.route("/registration")
def registration():
    with app.app_context():
        return render_template("registration.html")

@app.post("/token-create")
def tokenCreate():
    username = request.form['username']
    password = request.form['password']
   
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://13.212.226.116:8000/docs/")

    # Interact with the API endpoint
    action = ["api", "token > create"]
    params = {
        "username": username,
        "password": password,
        "token": secret_key2,
    }
    headers = {"Authorization": f"Bearer {token.decode('utf-8')}"}
    token = jwt.encode(params, secret_key1, algorithm="HS256")

    result = client.action(schema, action, params=headers)
    return result

@app.post("/token-refresh-create")
def tokenRefreshCreate():
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://13.212.226.116:8000/docs/")

    # Interact with the API endpoint
    action = ["api", "token > refresh > create"]
    params = {
        "refresh": ...,
    }
    result = client.action(schema, action, params=params)
    return result

@app.post("/article")
def article():
    limit = request.form['limit']
    offset = request.form['offset']
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://13.212.226.116:8000/docs/")

    # Interact with the API endpoint
    action = ["article", "list"]
    params = {
        "limit": limit,
        "offset": offset,
    }
    result = client.action(schema, action, params=params)
    return result

@app.post("/article/<id>")
def articleId():
    thisId = id
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://13.212.226.116:8000/docs/")

    # Interact with the API endpoint
    action = ["article", "read"]
    params = {
        "id": thisId,
    }
    result = client.action(schema, action, params=params)
    return result

@app.post("/profile")
def profile():
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://13.212.226.116:8000/docs/")

    # Interact with the API endpoint
    action = ["profile", "list"]
    result = client.action(schema, action)
    return result

@app.post("/register")
def register():
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    telephone = "+"+str(request.form['telephone'])
    profile_image = request.form['profile_image']
    address = request.form['address']
    city = request.form['city']
    province = request.form['province']
    country = request.form['country']

    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://13.212.226.116:8000/docs/")

    # Interact with the API endpoint
    action = ["register", "create"]
    params = {
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "telephone": telephone,
        "profile_image": profile_image,
        "address": address,
        "city": city,
        "province": province,
        "country": country,
        "token": secret_key2,
    }
    headers = {"Authorization": f"Bearer {token.decode('utf-8')}"}
    token = jwt.encode(params, secret_key1, algorithm="HS256")

    result = client.action(schema, action, params=headers)
    return result