from Models.Blockchain import Blockchain
from Database import Repositories as DB
from Network import WSBlockChainSync
from Middleware import JSONWorker
from Models.Blockchain import Blockchain
import asyncio
def SynchronizeBlockChain():
    data  = DB.GetNetworkData()
    nodes = data["Nodes"]
    latency_nodes = {k: v for k, v in nodes.items() if "Latency" in v}
    if latency_nodes:
        closest_node = min(latency_nodes.items(), key=lambda item: item[1]["Latency"])
        closest_ip = closest_node[0]
        ReceivedChain = WSBlockChainSync.SynchronizeHandler(closest_ip)
        if(ReceivedChain["BlockChainData"] != '' and ReceivedChain["BlockChainData"]):
            JSONWorker.CreateDataJSON('Database/BlockChainDB.json',ReceivedChain["BlockChainData"])
    else:
        print("No nodes with latency information found.")

def VerifySyncBlockChain():
    BlockChain:Blockchain = Blockchain()
    if(not BlockChain.verify_chain()):
        SynchronizeBlockChain()
    else:
        return