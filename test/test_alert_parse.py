#! /usr/bin/env python
from alert_parser import AlertParser
from .dummy_data import *
import pytest


def test_load_correct_data():
    parser = AlertParser(testEntries)
    assert parser.alerts==testAlerts

def test_load_empty():
    parser = AlertParser([])
    assert parser.alerts == []

def test_get_all_alerts():
    parser = AlertParser(testEntries)
    response = generate_alert_response(5,testAlerts)
    assert parser.get_alerts(0,10,[]) ==response

def test_get_range_alerts():
    parser = AlertParser(testEntries)
    response = generate_alert_response(5,testAlerts[2:4])
    assert parser.get_alerts(2,2,[]) == response

def test_get_filtered_alerts():
    parser = AlertParser(testEntries)
    response = generate_alert_response(2,[testAlerts[0],testAlerts[3]])
    assert parser.get_alerts(0,10,[1,4]) == response

def test_get_agents():
    parser = AlertParser(testEntries)
    response = generate_agents_response(4,[generate_agent(21),2],[generate_agent(31),1])
    assert parser.get_agents(1,2) == response

def test_get_agent_by_id():
    parser = AlertParser(testEntries)
    response = generate_agent_id_response(generate_agent(21),[generate_alert(21,22,2),generate_alert(21,12,4)])
    assert parser.get_agent_by(21) == response

def test_get_rules():
    parser = AlertParser(testEntries)
    response = generate_rules_response(3,[generate_rule(22),1],[generate_rule(32),1])
    assert parser.get_rules(1,2) == response
def test_get_rule_by_id():
    parser = AlertParser(testEntries)
    response = generate_rule_id_response(generate_rule(12),[generate_alert(11,12,1),generate_alert(21,12,4),generate_alert(51,12,5)])
    assert parser.get_rule_by(12) == response