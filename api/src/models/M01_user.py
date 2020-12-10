from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db

ma = Marshmallow()

class M01_userModel(db.Model):
    __tablename__ = 'M01_user'

    user_id = db.Column(db.String(255), primary_key=True, nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=False)

    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id, pwd, mail, new_pwd, new_mail):
        self.user_id = user_id
        self.pwd = pwd
        self.mail = mail
        self.new_pwd = new_pwd
        self.new_mail = new_mail

    def __repr__(self):
        return '<M01_userModel {}:{}>'.format(self.user_id, self.pwd, self.mail, self.new_pwd, self.new_mail)

class M01_userSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = M01_userModel
        load_instance=True

    createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')