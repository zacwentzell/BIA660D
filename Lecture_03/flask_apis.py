from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify

app = Flask(__name__)
api = Api(app)


class Questions(Resource):
    def get(self):
        # Here is where you would answer the question in the request.
        return jsonify({'answer': 'You have to write the code for my brain...'})

class Statements(Resource):
    def post(self):
        # Here is where you would take in new data for the bot

        # data is available via the request variable
        return 'Data received! \n {}'.format(request.data)


api.add_resource(Questions, '/questions')
api.add_resource(Statements, '/statements')

if __name__ == '__main__':
    app.run(port=5002)