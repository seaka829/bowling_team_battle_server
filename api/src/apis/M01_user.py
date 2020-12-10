from flask_restful import Resource, reqparse, abort
from flask import jsonify, request
from src.models.M01_user import M01_userModel, M01_userSchema
from src.database import db

class M01_userListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_id', required=True)
        self.reqparse.add_argument('pwd', required=True)
        self.reqparse.add_argument('mail', required=True)
        super(M01_userListAPI, self).__init__()
    
    def get(self):
        results = M01_userModel.query.all()
        jsonData = M01_userSchema(many=True).dump(results)
        return jsonify({'items': jsonData})

    def post(self):
        args = self.reqparse.parse_args()
        M01_user = M01_userModel(args.user_id, args.pwd, args.mail)
        db.session.add(M01_user)
        db.session.commit()
        res = M01_userSchema().dump(M01_user)
        return res, 201

class M01_userAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_id')
        self.reqparse.add_argument('pwd')
        self.reqparse.add_argument('mail')
        super(M01_userAPI, self).__init__()

    def get(self, user_id):
        args = self.reqparse.parse_args()
        input_pwd = args.pwd
        # ユーザーマスタからユーザー情報を取得
        M01_user = db.session.query(M01_userModel).filter_by(user_id=user_id, pwd=input_pwd).first()
        if M01_user is None:
            return jsonify({
                "message": "ユーザーIDまたはパスワードが間違っています。"
            })

        res = M01_userSchema().dump(M01_user)
        return res

    def post(self):
        args = self.reqparse.parse_args()
        input_pwd = args.pwd
        input_user_id = args.user_id
        # ユーザーマスタからユーザー情報を取得
        M01_user = db.session.query(M01_userModel).filter_by(user_id=input_user_id, pwd=input_pwd).first()
        # ユーザー情報を取得できなかった場合
        if M01_user is None:
            return jsonify({
                "message": "ユーザーIDまたはパスワードが間違っています。"
            })
        
        res = M01_userSchema().dump(M01_user)
        return res, 201


    