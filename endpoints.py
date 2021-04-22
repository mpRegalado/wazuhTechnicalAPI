from flask import Blueprint, jsonify, request

def create_blueprint_data(parser):
    endpoint = Blueprint("access_data",__name__)

    @endpoint.route("/alerts", methods=["GET"])
    def get_alerts():
        offset = request.json["offset"]
        limit = request.json["limit"]
        id = request.json["id"]

        response = parser.get_alerts(offset,limit,id)
        return jsonify(response)
    
    @endpoint.route("/agents", methods=["GET"])
    def get_agents():
        offset = request.json["offset"]
        limit = request.json["limit"]

        response = parser.get_agents(offset,limit)
        return jsonify(response)
    
    @endpoint.route("/agents/:<int:id>")
    def get_agent(id):
        response = parser.get_agent_by(id)

        return jsonify(response)

    @endpoint.route("/rules")
    def get_rules():
        offset = request.json["offset"]
        limit = request.json["limit"]

        response = parser.get_rules(offset,limit)
        return jsonify(response)

    @endpoint.route("/rules/:<int:id>")
    def get_rule(id):
        response = parser.get_rule_by(id)
        return jsonify(response)

    return endpoint