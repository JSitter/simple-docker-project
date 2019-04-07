from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify

app = Flask(__name__)
api = Api(app, version='1.0', title='Simple Flask App', description='This is a flask app for flasking things and apping')
ns = api.namespace('Flask-Space', description='Methodical methods')

single_parser = api.parser()

@ns.route('/')
class Index(Resource):
  ''' Main page.'''
  @api.doc(parser=single_parser, description='Get main page')
  def get(self):
    return {"Who did it?": "Don't Ask"}

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)