import asyncio
from Database import DB
from websockets.server import serve

async def Broadcast(websocket):
    async for message in websocket:
        await websocket.send(message)

async def Node():
    async with serve(Broadcast, "localhost", DB.GetUserData):
        await asyncio.Future()  # run forever

