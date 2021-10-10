from database.db import db
from .mbti_types import MbtiTypes
from .movies import Movies


class CharactersMbti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_gender = db.Column(db.String(6), nullable=False)
    character_name = db.Column(db.String(30), nullable=False)
    character_image_path = db.Column(db.TEXT, nullable=False)
    head_comment = db.Column(db.String(255), nullable=False)
    scripts = db.Column(db.TEXT, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    character_sub_image_path = db.Column(db.TEXT, nullable=False)
    recommendation = db.Column(db.TEXT, nullable=False)
    character_mbti = db.Column(db.String(4), db.ForeignKey("mbti_types.mbti_type"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))

    def __init__(
        self,
        character_gender,
        character_name,
        character_image_path,
        head_comment,
        scripts,
        description,
        character_sub_image_path,
        recommendation,
        character_mbti,
        movie_id,
    ):
        self.character_gender = character_gender
        self.character_name = character_name
        self.character_image_path = character_image_path
        self.head_comment = head_comment
        self.scripts = scripts
        self.description = description
        self.character_sub_image_path = character_sub_image_path
        self.recommendation = recommendation
        self.character_mbti = character_mbti
        self.movie_id = movie_id
