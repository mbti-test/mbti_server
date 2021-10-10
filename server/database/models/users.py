import datetime
from database.db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(6), nullable=False)
    answer = db.Column(db.String(12), nullable=False)
    user_mbti = db.Column(db.String(4), nullable=False)
    response_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_agent = db.Column(db.String(255))

    def __init__(self, gender, answer, user_mbti):
        self.gender = gender
        self.answer = answer
        self.user_mbti = user_mbti
