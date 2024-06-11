
def GetNetworkData(param):
        import json
        f = open('Database/Connection.json')
        data = json.load(f)
        return data    

def GetUserData(param):
        import json 
        f = open('Database/NodeDB.json')
        data = json.load(f)
        return data[param]    
