import asyncio
import json
from websockets.server import serve

async def Broadcast(websocket):
    async for message in websocket:
        await websocket.send(message)

async def Node():
    async with serve(Broadcast, "localhost", 8765):
        await asyncio.Future()  # run forever

