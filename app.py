#! /usr/bin/env python

from flask import Flask
from alert_parser import AlertParser
from endpoints import create_blueprint_data
import json

from test.dummy_data import generate_entry

def create_app(parser = AlertParser([])):
    app = Flask(__name__)
    app.register_blueprint(create_blueprint_data(parser))    
    return app

if __name__ == '__main__':
    with open('assets/alerts.json') as file:
        parser = AlertParser(json.load(file))
    app = create_app(parser)
    app.run()