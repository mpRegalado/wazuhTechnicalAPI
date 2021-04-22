from copy import deepcopy
class AlertParser:
    def __init__(self, entries):
        self.alerts = []
        for entry in entries:
            self.alerts.append(entry["_source"])

    def _filter_alerts(self, ids=[]):
        #The GET request may include a list of IDs as numbers, in that case, we only check the matching alerts.
        alerts = []
        for alert in self.alerts:
            if float(alert["id"]) in ids:
                alerts.append(alert)
        
        return alerts
    
    def get_alerts(self, offset,limit,ids):
        if offset < 0 or not isinstance(offset,int):
            raise ValueError("Offset must be a positive integer")

        if ids:
            alerts = deepcopy(self._filter_alerts(ids))
        else:
            alerts = deepcopy(self.alerts)
        
        return {
            "total_items": len(alerts),
            "data": alerts[offset:offset+limit]
        }

    def get_agents(self, offset,limit):
        if offset < 0 or not isinstance(offset,int):
            raise ValueError("Offset must be a positive integer")
        
        agents = {}
        for alert in self.alerts:
            agentID = alert["agent"]["id"]
            if agentID in agents:
                agents[agentID]["total_alerts"] += 1
            else:
                agents[agentID]=deepcopy(alert["agent"])
                agents[agentID]["total_alerts"] = 1

        return {
            "total_items": len(agents),
            "data" : list(agents.values())[offset:offset+limit]
        }
    def get_agent_by(self, id):
        agent = None
        for alert in self.alerts:
            agentID = alert["agent"]["id"]
            if agentID == str(id):
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

    def get_rules(self, offset,limit):
        if offset < 0 or not isinstance(offset,int):
            raise ValueError("Offset must be a positive integer")
        
        rules = {}
        for alert in self.alerts:
            ruleID = alert["rule"]["id"]
            if ruleID in rules:
                rules[ruleID]["total_alerts"] += 1
            else:
                rules[ruleID]=deepcopy(alert["rule"])
                rules[ruleID]["total_alerts"] = 1

        return {
            "total_items": len(rules),
            "data" : list(rules.values())[offset:offset+limit]
        }
    def get_rule_by(self, id):
        rule = None
        for alert in self.alerts:
            ruleID = alert["rule"]["id"]
            if ruleID == str(id):
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