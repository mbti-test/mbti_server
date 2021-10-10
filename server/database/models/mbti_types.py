from database.db import db


class MbtiTypes(db.Model):
    mbti_type = db.Column(db.String(4), primary_key=True)
    good_mbti = db.Column(db.String(4), nullable=False)
    bad_mbti = db.Column(db.String(4))

    def __init__(self, mbti_type, good_mbti, bad_mbti):
        self.mbti_type = mbti_type
        self.good_mbti = good_mbti
        self.bad_mbti = bad_mbti
