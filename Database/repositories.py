

def GetNetworkData():
    import json 
    f = open('network_db.json')
    data = json.load(f)
    return data