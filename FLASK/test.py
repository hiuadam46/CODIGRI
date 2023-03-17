from flask import render_template
from flask import Flask
import coreapi
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json

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

@app.route("/chats")
def chats():
    with app.app_context():
        return render_template("chats.html")

@app.route("/get-all-rooms")
def getAllRooms():
   with app.app_context():
      result = '['
      rooms = Room.query.all()
      for x in range(len(rooms)):
            if(x==0):
               result += '{'
            else:
               result += ',{'
            result += '"ID":'+str(rooms[x].id)
            result += ',"NAME":"'+str(rooms[x].name)+'"'
            result += '}'
      result += ']'
      return result
      

@app.route("/get-all-users")
def getAllUsers():
   with app.app_context():
        result = '['
        users = User.query.all()
        for x in range(len(users)):
            if(x==0):
               result += '{'
            else:
               result += ',{'
            result += '"ID":'+str(users[x].id)
            result += ',"USERNAME":"'+str(users[x].username)+'"'
            result += ',"NAME":"'+str(users[x].name)+'"'
            result += '}'
        result += ']'
        return result

@app.route("/get-all-chats-by-room/<id>")
def getAllChatsByRoom(id):
   with app.app_context():
        chats = db.session.query(Chat.message, Room.name, User.name).\
            join(Room, Chat.id_room == Room.id).\
            join(User, Chat.id_user == User.id).\
            filter(Chat.id_room == id).\
            order_by(Chat.id.desc()).all()
        
   result = '['
   init = 0
   for chat, room_name, user_name in chats:
      if(init == 0):
         result += '{'
      else:
          result += ',{'
      result += '"NAME":"'+user_name+'"'
      result += ',"ROOM":"'+room_name+'"'
      result += ',"MESSAGE":"'+chat+'"'
      result += '}'
      init += 1
   result += ']'
   return result

@app.route("/init")
def init():
    initThis()
    return "Success!"

def initThis():
   db.create_all()
    
   # user = User(name='Awd', username='hiuadam96')
   # room = Room(name='General')
   # chat = Chat(id_user=1, id_room=1, message="awidowaihd")
   # chat = Chat(id_user=2, id_room=1, message="GEGE")

   # db.session.add(user)
   # db.session.add(room)
   # db.session.add(chat)
   # db.session.commit()