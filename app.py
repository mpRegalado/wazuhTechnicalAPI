#! /usr/bin/env python

from flask import Flask
from flask_cors import CORS, cross_origin
from alert_parser import AlertParser
from endpoints import create_blueprint_data
import json

def create_app(parser = AlertParser([])):
    app = Flask(__name__)
    app.register_blueprint(create_blueprint_data(parser))
    CORS(app=app, resources={r"/*": {"origins": "*"}})
    return app

with open('assets/alerts.json') as file:
    parser = AlertParser(json.load(file))
app = create_app(parser)
if __name__ == '__main__':
    app.run()