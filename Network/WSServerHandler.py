import asyncio
import websockets
from Middleware import BlockChainSync
from Database import Repositories as DB
from Middleware import JSONWorker
from Controller import BlockReceiverController
import socket, json, time, datetime
CONNECTIONS = set()
from urllib.parse import urlparse

async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        pass
async def broadcast(message):
    for websocket in CONNECTIONS:
        asyncio.create_task(send(websocket, message))
async def Broadcast_messages():
    while True:
        await asyncio.sleep(1)
        data = JSONWorker.GetDataJSON('Buffer/WaitBox.json')
        if(data["Draft"] != None and data["Draft"] != "" and data["Draft"] != ''):
            print("Broadcast a Block ...", data["Draft"])
            await broadcast(json.dumps(data["Draft"]))
            JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":""})
            

async def Register(websocket):
    client_host = websocket.remote_address[0]
    start_time = time.time()
    await websocket.ping()
    await websocket.recv()
    latency = time.time() - start_time
    dict = {"IP":client_host,
            "LastChanged":str(datetime.datetime.now()),
            "Latency":latency,
            "Status":"Online"
            }
    DB.CreateNetworkData(client_host, dict)
async def Handler(websocket):
    CONNECTIONS.add(websocket)
    await Register(websocket)
    await Broadcast_messages()
    try:
        await websocket.wait_closed()
        client_host = websocket.remote_address[0]
        NetData = DB.GetNetworkData()
        dict = {"IP":client_host,
            "LastChanged":str(datetime.datetime.now()),
            "Latency":NetData["Nodes"][client_host]["Latency"],
            "Status":"Offline"
            }
        DB.CreateNetworkData(client_host, dict)
    finally:
        print("Connection Offline")
        CONNECTIONS.remove(websocket)
        client_host = websocket.remote_address[0]
        NetData = DB.GetNetworkData()
        dict = {"IP":client_host,
            "LastChanged":str(datetime.datetime.now()),
            "Latency":NetData["Nodes"][client_host]["Latency"],
            "Status":"Offline"
            }
        DB.CreateNetworkData(client_host, dict)
async def HandlerGetBlockChain(websocket, path):
        BlockChainSync.VerifySyncBlockChain()
        BlockChainData = DB.GetBlockChainData()
        UserData = DB.GetUserData("PublicKey")
        ConnectionData = DB.GetNetworkData()
        await websocket.send(json.dumps({
            "WalletAuthor":UserData,
            "NetworkData":ConnectionData,
            "BlockChainData" : BlockChainData}))
async def route(websocket, path):
    parsed_path = urlparse(path)
    route_path = parsed_path.path
    if route_path == "/get-blockchaindata":
        await HandlerGetBlockChain(websocket, path)
    else:
         await Handler(websocket)
         

async def main():
    hostname = socket.gethostname()
    NodeAddress = socket.gethostbyname(hostname)
    JSONWorker.EditDataJSON('Database/NodeDB.json',"NodeAddress",NodeAddress)
    print("Server Network Panel : ")
    async with websockets.serve(route, DB.GetUserData("NodeAddress"), 8333):
        # print("Server Is Starting ... ")
        await asyncio.Future()
