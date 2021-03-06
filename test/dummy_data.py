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
        "id": str(alertID),
        "uid":str(alertID)
    }

def generate_entry(agentID, ruleID, alertID):
    return {
        "_id": str(alertID),
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

testEntries = [
    generate_entry(11,12,1),
    generate_entry(21,22,2),
    generate_entry(31,32,3),
    generate_entry(21,12,4),
    generate_entry(51,12,5)
]
testAlerts = [
    generate_alert(11,12,1),
    generate_alert(21,22,2),
    generate_alert(31,32,3),
    generate_alert(21,12,4),
    generate_alert(51,12,5)
]