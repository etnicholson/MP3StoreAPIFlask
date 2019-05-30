from application import app, db, api
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from flask_restplus import Resource

@app.route("/")
@app.route("/index")

def index():
    return "Hello"



class Mp3 (db.Document):
    artist =   db.StringField( max_length = 200 )
    song   =   db.StringField( max_length = 200 )
    label  =   db.StringField( max_length = 200 )


@app.route("/mp3")
def mp3():
    Mp3(artist="Tchami",song= "2", label= "Confession").save()

    return jsonify(Mp3.objects.all())


