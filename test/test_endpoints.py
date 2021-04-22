#! /usr/bin/env python
from .dummy_data import *
import unittest, requests
import pdb

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
        self.maxDiff = 1500


    
    def test_get_all_alerts(self):
        api_response = requests.get("http://127.0.0.1:5000/alerts",json={
            "offset":0,
            "limit":10,
            "id":[]
        })
        response = generate_alert_response(5,self.correctAlerts)
        self.assertEqual(api_response.json(),response)
    def test_get_range_alerts(self):
        api_response = requests.get("http://127.0.0.1:5000/alerts",json={
            "offset":2,
            "limit":2,
            "id":[]
        })
        response = generate_alert_response(5,self.correctAlerts[2:4])
        self.assertEqual(api_response.json(),response)
    def test_get_filtered_alerts(self):
        api_response = requests.get("http://127.0.0.1:5000/alerts",json={
            "offset":0,
            "limit":10,
            "id":[1,4]
        })
        response = generate_alert_response(2,[self.correctAlerts[0],self.correctAlerts[3]])
        self.assertEqual(api_response.json(),response)

    def test_get_agents(self):
        api_response = requests.get("http://127.0.0.1:5000/agents",json={
            "offset":1,
            "limit":2
        })
        response = generate_agents_response(4,[generate_agent(21),2],[generate_agent(31),1])
        self.assertEqual(api_response.json(),response)
    def test_get_agent_by_id(self):
        api_response = requests.get("http://127.0.0.1:5000/agents/:21")
        response = generate_agent_id_response(generate_agent(21),[generate_alert(21,22,2),generate_alert(21,12,4)])
        self.assertEqual(api_response.json(),response)

    def test_get_rules(self):
        api_response = requests.get("http://127.0.0.1:5000/rules",json={
            "offset":1,
            "limit":2
        })
        response = generate_rules_response(3,[generate_rule(22),1],[generate_rule(32),1])
        self.assertEqual(api_response.json(),response)
    def test_get_rule_by_id(self):
        api_response = requests.get("http://127.0.0.1:5000/rules/:12")
        response = generate_rule_id_response(generate_rule(12),[generate_alert(11,12,1),generate_alert(21,12,4),generate_alert(51,12,5)])
        self.assertEqual(api_response.json(),response)

if __name__ == '__main__':
    unittest.main()