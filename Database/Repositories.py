from Middleware import JSONWorker, KeyGenerator
def GetNetworkData():
        return JSONWorker.GetDataJSON('Database/ConnectionDB.json')
def GetUserData(param = ''):
        data =  JSONWorker.GetDataJSON('Database/NodeDB.json')
        if(param == ''):
              return data
        return data[param]
def GetBlockChainData():
        return JSONWorker.GetDataJSON('Database/BlockChainDB.json')
def CreateNetworkData(NodeAddress, param):
    NetworkData = GetNetworkData()["Nodes"]
    NetworkData[NodeAddress] = param
    return JSONWorker.CreateDataJSON('Database/ConnectionDB.json',{"Nodes":NetworkData})
def CreateBlockChainData(param):
    return JSONWorker.CreateDataJSON('Database/BlockChainDB.json',param)[-1]
# Repositories

