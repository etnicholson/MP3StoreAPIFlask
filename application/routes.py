from application import app, db, api
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from flask_restplus import Resource
from application.models import Mp3


@api.route('/api','/api/')
class GetAndPost(Resource):

    #GET ALL
    def get(self):
        return jsonify(Mp3.objects.all())

    #POST
    def post(self):
        data= api.payload
        mp3 = Mp3(artist=data['artist'],song=data['song'],label=data['label'])
        mp3.save()
        return jsonify(mp3)



@api.route('/api/<objectid:oid>')
class GetUpdateDelete(Resource):

    #GET ONE
    def get(self,oid):
        return jsonify(Mp3.objects(id=oid))