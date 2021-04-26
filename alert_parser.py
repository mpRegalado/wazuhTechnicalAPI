from copy import deepcopy
import pdb
class AlertParser:
    def __init__(self, entries):
        self.entries = deepcopy(entries)
        self.alerts = []
        for entry in self.entries:
            alert = deepcopy(entry["_source"])
            alert["uid"]=entry["_id"]           
            self.alerts.append(alert)

    def get_alerts(self, offset=0,limit=0,ids=[]):
        if ids:
            alerts = deepcopy([alert for alert in self.alerts if int(alert["id"]) in ids])
        else:
            alerts = deepcopy(self.alerts)
        
        if (limit == 0):
            data = alerts[offset:]
        else:
            data = alerts[offset:offset+limit]
        return {
            "total_items": len(alerts),
            "data": data
        }

    def get_agents(self, offset=0,limit=0):
        agents = {}
        for alert in self.alerts:
            agentID = alert["agent"]["id"]
            if agentID in agents:
                agents[agentID]["total_alerts"] += 1
            else:
                agents[agentID]=deepcopy(alert["agent"])
                agents[agentID]["total_alerts"] = 1

        if (limit == 0):
            data = list(agents.values())[offset:]
        else:
            data = list(agents.values())[offset:offset+limit]
        return {
            "total_items": len(agents),
            "data" : data
        }
    def get_agent_by(self, id):
        agent = None
        for alert in self.alerts:
            agentID = int(alert["agent"]["id"])
            if agentID == id:
                if agent is None:
                    agent = deepcopy(alert["agent"])
                    agent["alerts"]=[alert]
                else:
                    agent["alerts"].append(alert)
        if agent is not None:
            agent["total_alerts"]=len(agent["alerts"])
        
        return {
            "data" : agent
        }

    def get_rules(self, offset=0,limit=0):
        rules = {}
        for alert in self.alerts:
            ruleID = alert["rule"]["id"]
            if ruleID in rules:
                rules[ruleID]["total_alerts"] += 1
            else:
                rules[ruleID]=deepcopy(alert["rule"])
                rules[ruleID]["total_alerts"] = 1

        if (limit == 0):
            data = list(rules.values())[offset:]
        else:
            data = list(rules.values())[offset:offset+limit]
        return {
            "total_items": len(rules),
            "data" : data
        }
    def get_rule_by(self, id):
        rule = None
        for alert in self.alerts:
            ruleID = int(alert["rule"]["id"])
            if ruleID == id:
                if rule is None:
                    rule = deepcopy(alert["rule"])
                    rule["alerts"]=[alert]
                else:
                    rule["alerts"].append(alert)
        
        if rule is not None:
            rule["total_alerts"] = len(rule["alerts"])
        
        return {
            "data" : rule
        }