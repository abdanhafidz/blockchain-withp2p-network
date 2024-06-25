import asyncio
import websockets
from websockets.sync.client import connect
from Models.Interface import Block
from Database import Repositories as DB
from Middleware import JSONWorker
import json

def SynchronizeHandler(address):
      with connect(f"ws://{address}:8333/get-blockchaindata") as websocket:
        while True:
            websocket.ping()
            message = websocket.recv()
            if(message != ""):
                data = json.loads(message)
                return data
                
