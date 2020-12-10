from flask import Flask, jsonify, session, request
from flask_restful import Api
from src.database import init_db
from src.apis.M01_user import M01_userListAPI, M01_userAPI
from src.util import random_string

def create_app():
    app = Flask(__name__)
    app.secret_key = 'app secret key'
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object('src.config.Config')

    init_db(app)

    api = Api(app)
    api.add_resource(M01_userListAPI, '/v1/api')
    api.add_resource(M01_userAPI, '/v1/api/login')

    return app

app = create_app()