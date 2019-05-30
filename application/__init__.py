from flask import Flask

from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api

from flask_objectid_converter import ObjectIDConverter


api = Api()

app = Flask(__name__)
app.config.from_object(Config)

app.url_map.converters['objectid'] = ObjectIDConverter


db = MongoEngine()
db.init_app(app)
api.init_app(app)

from application import routes

