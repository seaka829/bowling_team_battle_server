from flask import Flask, jsonify, session, request
from util import random_string


app = Flask(__name__)
app.secret_key = 'app secret key'
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return jsonify({
        "message": random_string(100)
    })

@app.route('/login')
def login():
    session.permanent = True
    #app.permanent_session_lifetime = timedelta(minutes=30)
    if session["user_id" ] is not None:
        session["user_id"] = request.args.get('user_id')
        return jsonify({
            "state": "login success"
            ,"user_id": request.args.get('user_id')
        })
    else:
        return jsonify({
            "state": "logined"
            ,"user_id": request.args.get('user_id')
        })
    
@app.route('/logout')
def logout():
    if session["user_id"] is not None:
        session["user_id"] = None
        return "logout"
    else:
        return "not login"

@app.route('/create_room_id', methods=["POST"])
def create_room_id():
    return jsonify({
        "room_id": "qwertyuiopasdfghjklz"
    })

@app.route('/enter_room', methods=["POST"])
def enter_room():
    return jsonify({
        "test": "11"
    })

if __name__ == '__main__':
    app.run()