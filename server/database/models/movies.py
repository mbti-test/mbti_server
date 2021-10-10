from database.db import db


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_link = db.Column(db.TEXT, nullable=False)

    def __init__(self, movie_title, movie_link):
        self.movie_title = movie_title
        self.movie_link = movie_link
