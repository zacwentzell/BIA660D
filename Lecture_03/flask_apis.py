from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


class Questions(Resource):
    def get(self):
        # Here is where you would answer the question in the request.
        return jsonify({'answer': 'You have to write the code for my brain...'})

class Statements(Resource):
    def post(self):
        # Here is where you would take in new data for the bot
        return 'Data received!'


api.add_resource(Questions, '/questions')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')