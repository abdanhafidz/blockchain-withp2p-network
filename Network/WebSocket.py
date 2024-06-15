import asyncio
import random
import websockets
from Models.Block import Block
from Database import Repositories as DB
from Engine import JSONWorker
import json
CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    client_host = websocket.client.host
    if(not DB.GetNetworkData["Nodes"][client_host]):
                dict = {
                    "{addr}" : {
                    "IP":client_host,
                    "LastChanged":""
                    }
                }
    DB.CreateNetworkData(dict)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def send(data):
    while True:
        websockets.broadcast(CONNECTIONS, data)
        await asyncio.sleep(random.random() * 2 + 1)

async def main():
    try:
        async with websockets.serve(register, "localhost", 8333):
            data = JSONWorker.GetDataJSON('Buffer/WaitBox.json')
            if(data["Draft"] != None and data["Draft"] != "" and data["Draft"] != ''):
                print("Broadcast a Block ...", data["Draft"])
                await send(str(data["Draft"]))
                print(JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":""}))
    except Exception as err:
         print("Websocket Error : ",err)
         return err
        

