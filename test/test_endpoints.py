#! /usr/bin/env python
import pytest

from .dummy_data import *
from app import create_app
from alert_parser import AlertParser

@pytest.fixture
def client():
    parser = AlertParser(testEntries)
    app = create_app(parser)
    with app.test_client() as client:
        yield client
    
def test_get_all_alerts(client):
    api_response = client.get("/alerts",query_string={
        "offset":0,
        "limit":10,
        "id":[]
    }).json
    response = generate_alert_response(5,testAlerts)
    assert api_response == response

def test_get_range_alerts(client):
    api_response = client.get("/alerts",query_string={
        "offset":2,
        "limit":2
    }).json
    response = generate_alert_response(5,testAlerts[2:4])
    assert api_response == response

def test_get_filtered_alerts(client):
    api_response = client.get("/alerts",query_string={
        "offset":0,
        "limit":10,
        "id":"1,4"
    }).json
    response = generate_alert_response(2,[testAlerts[0],testAlerts[3]])
    assert api_response == response

def test_get_agents(client):
    api_response = client.get("/agents",query_string={
        "offset":1,
        "limit":2
    }).json
    response = generate_agents_response(4,[generate_agent(21),2],[generate_agent(31),1])
    assert api_response == response
def test_get_agent_by_id(client):
    api_response = client.get("/agents/:21").json
    response = generate_agent_id_response(generate_agent(21),[generate_alert(21,22,2),generate_alert(21,12,4)])
    assert api_response == response

def test_get_rules(client):
    api_response = client.get("/rules",query_string={
        "offset":1,
        "limit":2
    }).json
    response = generate_rules_response(3,[generate_rule(22),1],[generate_rule(32),1])
    assert api_response == response

def test_get_rule_by_id(client):
    api_response = client.get("/rules/:12").json
    response = generate_rule_id_response(generate_rule(12),[generate_alert(11,12,1),generate_alert(21,12,4),generate_alert(51,12,5)])
    assert api_response == response