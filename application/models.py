import flask
from application import db

class Mp3 (db.Document):
    artist =   db.StringField( max_length = 200 )
    song   =   db.StringField( max_length = 200 )
    label  =   db.StringField( max_length = 200 )