from flask import Blueprint, jsonify, request
import pdb

def corsDecorator(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return wrapper

def create_blueprint_data(parser):
    endpoint = Blueprint("access_data",__name__)

    @endpoint.route("/alerts", methods=["GET"])
    def get_alerts():
        offset = int(request.args.get("offset"))
        limit = int(request.args.get("limit"))
        if(request.args.get("id")):
            id = request.args.get("id")
            id = [float(i) for i in id.split(',')]
        else:
            id = []

        response = jsonify(parser.get_alerts(offset,limit,id))
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
    @endpoint.route("/agents", methods=["GET"])
    def get_agents():
        offset = int(request.args.get("offset"))
        limit = int(request.args.get("limit"))

        response = jsonify(parser.get_agents(offset,limit))
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    
    @endpoint.route("/agents/:<int:id>")
    def get_agent(id):
        jsonify(response = parser.get_agent_by(id))

        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    @endpoint.route("/rules")
    def get_rules():
        offset = int(request.args.get("offset"))
        limit = int(request.args.get("limit"))
        response = jsonify(parser.get_rules(offset,limit))
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    @endpoint.route("/rules/:<int:id>")
    def get_rule(id):
        response = jsonify(parser.get_rule_by(id))
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    return endpoint