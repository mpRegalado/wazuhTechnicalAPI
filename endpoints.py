from flask import Blueprint, jsonify, request
import pdb
from flask_cors import cross_origin

def corsDecorator(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return wrapper

def create_blueprint_data(parser):
    endpoint = Blueprint("access_data",__name__)

    @endpoint.route("/alerts", methods=["GET"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_alerts():
        offset = int(request.args.get("offset"))
        limit = int(request.args.get("limit"))
        if(request.args.get("id")):
            id = request.args.get("id")
            id = [float(i) for i in id.split(',')]
        else:
            id = []

        response = parser.get_alerts(offset,limit,id)
        return jsonify(response)
    
    @endpoint.route("/agents", methods=["GET"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_agents():
        offset = int(request.args.get("offset"))
        limit = int(request.args.get("limit"))

        response = parser.get_agents(offset,limit)
        return jsonify(response)
    
    @endpoint.route("/agents/:<int:id>")
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_agent(id):
        response = parser.get_agent_by(id)

        return jsonify(response)

    @endpoint.route("/rules")
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_rules():
        offset = int(request.args.get("offset"))
        limit = int(request.args.get("limit"))
        response = parser.get_rules(offset,limit)
        return jsonify(response)

    @endpoint.route("/rules/:<int:id>")
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_rule(id):
        response = parser.get_rule_by(id)
        return jsonify(response)

    return endpoint