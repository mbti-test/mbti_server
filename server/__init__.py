import os
import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from resources.mbti import Mbti
from database.db import db

migrate = Migrate()


def create_app():
    # Flask 객체 app 생성 및 config 변수 적용
    app = Flask(__name__)
    CORS(app)
    # app object에 config 적용
    app.config.from_object(config)
    # api 설정 및 적용
    api = Api(app)
    api.add_resource(Mbti, "/mbti", "/mbti/<user_mbti>/<gender>")
    # db 적용 및 migrate
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app, db)

    return app
