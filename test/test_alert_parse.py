#! /usr/bin/env python
from alert_parser import AlertParser
import unittest

def generate_rule(ruleID):
    return {
        "id": str(ruleID),
        "Description": "A rule" + str(ruleID)
    }

def generate_agent(agentID):
    return {
        "id": str(agentID),
        "name": "agent" + str(agentID),
        "ip": "someIP"
    }

def generate_alert(agentID, ruleID, alertID):
    return {
        "rule": generate_rule(ruleID),
        "agent": generate_agent(agentID),
        "id": str(alertID)
    }

def generate_entry(agentID, ruleID, alertID):
    return {
        "_id": "001",
        "_source" : generate_alert(agentID,ruleID,alertID)
    }

def generate_alert_response(total_items,data_array):    
    response = {
        "total_items": total_items,
        "data": data_array
    }
    return response
def generate_agents_response(total_items, *agentAlertPair):
    data = []
    for pair in agentAlertPair:
        item, count = pair
        data.append({
            **item,
            "total_alerts": count
        })
    
    return {
        "total_items": total_items,
        "data": data
    }

def generate_agent_id_response(agent,alertArray):
    return {
        "data": {
            **agent,
            "total_alerts": len(alertArray),
            "alerts": alertArray
        }
    }

def generate_rules_response(total_items, *ruleAlertPair):
    data = []
    for item in ruleAlertPair:
        data.append({
            **item[0],
            "total_alerts": item[1]
        })
    
    return {
        "total_items": total_items,
        "data": data
    }

def generate_rule_id_response(rule,alertArray):
    return {
        "data": {
            **rule,
            "total_alerts": len(alertArray),
            "alerts": alertArray
        }
    }

class TestAlertParse(unittest.TestCase):
    def setUp(self):
        self.correctData = [
            generate_entry(11,12,1),
            generate_entry(21,22,2),
            generate_entry(31,32,3),
            generate_entry(21,12,4),
            generate_entry(51,12,5)
        ]
        self.correctAlerts = [
            generate_alert(11,12,1),
            generate_alert(21,22,2),
            generate_alert(31,32,3),
            generate_alert(21,12,4),
            generate_alert(51,12,5)
        ]
        self.maxDiff = 1000

    
    def test_load_correct_data(self):
        parser = AlertParser(self.correctData)
        self.assertEqual(parser.alerts,self.correctAlerts)
    def test_load_empty(self):
        parser = AlertParser([])
        self.assertEqual(parser.alerts,[])

    def test_get_all_alerts(self):
        parser = AlertParser(self.correctData)
        response = generate_alert_response(5,self.correctAlerts)
        self.assertEqual(parser.get_alerts(0,10,[]),response)
    def test_get_range_alerts(self):
        parser = AlertParser(self.correctData)
        response = generate_alert_response(5,self.correctAlerts[2:4])
        self.assertEqual(parser.get_alerts(2,2,[]),response)
    def test_get_filtered_alerts(self):
        parser = AlertParser(self.correctData)
        response = generate_alert_response(2,[self.correctAlerts[0],self.correctAlerts[3]])
        self.assertEqual(parser.get_alerts(0,10,[1,4]),response)

    def test_get_agents(self):
        parser = AlertParser(self.correctData)
        response = generate_agents_response(4,[generate_agent(21),2],[generate_agent(31),1])
        self.assertEqual(parser.get_agents(1,2),response)
    def test_get_agent_by_id(self):
        parser = AlertParser(self.correctData)
        response = generate_agent_id_response(generate_agent(21),[generate_alert(21,22,2),generate_alert(21,12,4)])
        self.assertEqual(parser.get_agent_by(21),response)

    def test_get_rules(self):
        parser = AlertParser(self.correctData)
        response = generate_rules_response(3,[generate_rule(22),1],[generate_rule(32),1])
        self.assertEqual(parser.get_rules(1,2),response)
    def test_get_rule_by_id(self):
        parser = AlertParser(self.correctData)
        response = generate_rule_id_response(generate_rule(12),[generate_alert(11,12,1),generate_alert(21,12,4),generate_alert(51,12,5)])
        self.assertEqual(parser.get_rule_by(12),response)

if __name__ == '__main__':
    unittest.main()