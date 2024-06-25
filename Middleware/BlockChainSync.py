from Models.Blockchain import Blockchain
from Database import Repositories as DB
from Network import WSBlockChainSync
from Middleware import JSONWorker
from Models.Blockchain import Blockchain
import asyncio
def SynchronizeBlockChain():
    BlockChain = Blockchain()
    data  = DB.GetNetworkData()
    nodes = data["Nodes"]
    latency_nodes = {k: v for k, v in nodes.items() if "Latency" in v}
    sorted_nodes = sorted(latency_nodes.items(), key=lambda item: item[1]["Latency"])
    nodeIndex = 0
    while True:

        if latency_nodes:
            closest_node = sorted_nodes[nodeIndex]
            closest_ip = closest_node[0]
            print(closest_ip)
            if(closest_node[1]['Status'] == 'Offline'):
                nodeIndex+=1
                continue
            ReceivedChain = WSBlockChainSync.SynchronizeHandler(closest_ip)
            print("Synchronize to", closest_ip)
            if(ReceivedChain["BlockChainData"] != '' and ReceivedChain):
                if(BlockChain.verify_chain(ReceivedChain["BlockChainData"])):
                    JSONWorker.CreateDataJSON('Database/BlockChainDB.json',ReceivedChain["BlockChainData"])
                    break
                else:
                    nodeIndex+=1
                    continue

        else:
            print("No nodes with latency information found.")

def VerifySyncBlockChain():
    BlockChain:Blockchain = Blockchain()
    if(not BlockChain.verify_chain()):
        SynchronizeBlockChain()
    else:
        return