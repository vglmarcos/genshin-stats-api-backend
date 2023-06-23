import json
from flask import Flask, Response
from flask_restful import Api, Resource
import genshinstats as gs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

ltuid = 0
token = ""

class AllAPI(Resource):
    def __init__(self):
        self.ltuid = ltuid
        self.token = token
        gs.set_cookie(ltuid=self.ltuid, ltoken=self.token)

    def get(self, uid):
        try:
            all = gs.get_all_user_data(uid)
            data = {
                "message": "ok",
                "data": all
            }
            res = Response(json.dumps(data), status=200, mimetype='application/json')
            return res
        except gs.errors.AccountNotFound:
            data = {
                "message": "User Not Found",
                "data": {}
            }
            res = Response(json.dumps(data), status=404, mimetype='application/json')
            return res

class CharacteresAPI(Resource):
    def __init__(self):
        self.ltuid = ltuid
        self.token = token
        gs.set_cookie(ltuid=self.ltuid, ltoken=self.token)

    def get(self, uid):
        try:
            characteres = gs.get_characters(uid)
            data = {
                "message": "ok",
                "data": characteres
            }
            res = Response(json.dumps(data), status=200, mimetype='application/json')
            return res
        except gs.errors.AccountNotFound:
            data = {
                "message": "User Not Found",
                "data": []
            }
            res = Response(json.dumps(data), status=404, mimetype='application/json')
            return res
        
class NotesAPI(Resource):
    def __init__(self):
        self.ltuid = ltuid
        self.token = token
        gs.set_cookie(ltuid=self.ltuid, ltoken=self.token)

    def get(self, uid):
        try:
            resine = gs.get_notes(uid)
            data = {
                "message": "ok",
                "data": resine
            }
            res = Response(json.dumps(data), status=200, mimetype='application/json')
            return res
        except gs.errors.AccountNotFound:
            data = {
                "message": "User Not Found",
                "data": {}
            }
            res = Response(json.dumps(data), status=404, mimetype='application/json')
            return res

class SpiralAbyssAPI(Resource):
    def __init__(self):
        self.ltuid = ltuid
        self.token = token
        gs.set_cookie(ltuid=self.ltuid, ltoken=self.token)

    def get(self, uid):
        try:
            spiralAbyss = gs.get_spiral_abyss(uid)
            data = {
                "message": "ok",
                "data": spiralAbyss
            }
            res = Response(json.dumps(data), status=200, mimetype='application/json')
            return res
        except gs.errors.AccountNotFound:
            data = {
                "message": "User Not Found",
                "data": {}
            }
            res = Response(json.dumps(data), status=404, mimetype='application/json')
            return res
        
class UserStatsAPI(Resource):
    def __init__(self):
        self.ltuid = ltuid
        self.token = token
        gs.set_cookie(ltuid=self.ltuid, ltoken=self.token)

    def get(self, uid):
        try:
            userStats = gs.get_user_stats(uid)["stats"]
            data = {
                "message": "ok",
                "data": userStats
            }
            res = Response(json.dumps(data), status=200, mimetype='application/json')
            return res
        except gs.errors.AccountNotFound:
            data = {
                "message": "User Not Found",
                "data": {}
            }
            res = Response(json.dumps(data), status=404, mimetype='application/json')
            return res

api.add_resource(CharacteresAPI, '/genshinstats/<string:uid>/characteres/', endpoint = 'characteres')
api.add_resource(AllAPI, '/genshinstats/<string:uid>/all/', endpoint = 'all')
api.add_resource(NotesAPI, '/genshinstats/<string:uid>/notes/', endpoint = 'notes')
api.add_resource(SpiralAbyssAPI, '/genshinstats/<string:uid>/spiralabyss/', endpoint = 'spiralabyss')
api.add_resource(UserStatsAPI, '/genshinstats/<string:uid>/userstats/', endpoint = 'userstats')

if __name__ == "__main__":
    app.run(debug=True)