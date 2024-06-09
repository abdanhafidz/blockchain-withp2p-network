
class Database:
    def GetNetworkData():
        import json
        f = open('network_db.json')
        data = json.load(f)
        return data

    def GetUserData():
        import json 
        f = open('user_db.json')
        data = json.load(f)
        return data
    
DB = Database()