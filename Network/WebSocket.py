import asyncio
import random
import websockets
from Models.Block import Block
from Database import Repositories as DB
from Engine import JSONWorker
import json
CONNECTIONS = set()
import asyncio
import websockets
async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        pass
async def register(websocket):
    CONNECTIONS.add(websocket)
    client_host = websocket.remote_address[0]
    dict = {"IP":client_host,"LastChanged":""}
    DB.CreateNetworkData(client_host, dict)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def broadcast(message):
    for websocket in CONNECTIONS:
        asyncio.create_task(send(websocket, message))
async def broadcast_messages(message:str):
            await broadcast(message)
async def main():
    async with websockets.serve(register, "localhost", 8333):
        print("Start the Server")
        while True:
            await asyncio.sleep(1)
            data = JSONWorker.GetDataJSON('Buffer/WaitBox.json')
            if(data["Draft"] != None and data["Draft"] != "" and data["Draft"] != ''):
                print("Broadcast a Block ...", data["Draft"])
                await broadcast_messages(str(data["Draft"]))
                print(JSONWorker.CreateDataJSON('Buffer/WaitBox.json',{"Draft":""}))
                
