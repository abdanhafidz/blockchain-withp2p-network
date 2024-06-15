from Engine import JSONWorker
def GetNetworkData(param):
        return JSONWorker.GetDataJSON('Database/ConnectionDB.json')

def GetUserData(param):
        return JSONWorker.GetDataJSON('Database/NodeDB.json')

def CreateNetworkData(param):
    NetworkData = list(GetNetworkData["Nodes"])
    NetworkData.append(param)
    return JSONWorker.CreateDataJSON('Database/NodeDB.json',NetworkData)
