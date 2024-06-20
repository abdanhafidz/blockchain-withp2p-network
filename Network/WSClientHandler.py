import asyncio
import websockets
from Database import Repositories as DB
from Controller import BlockReceiverController
import json

TIMEOUT = 10

connected_nodes_set = set()

async def ClientHandler(address):
    try:
        async with websockets.connect(f"ws://{address}:8333") as websocket:
            print(f"Connection to {address} succeeded")
            connected_nodes_set.add(address)  # Tandai bahwa node berhasil terkoneksi
            while True:
                message = await websocket.recv()
                if message:
                    ReceivedBlock = json.loads(message)
                    BlockReceiverController.Control(ReceivedBlock)
        
    except asyncio.exceptions.TimeoutError:
        print(f"Connection to {address} timed out")
    except websockets.exceptions.ConnectionClosedError:
        if address in connected_nodes_set:
            print(f"Connection to {address} closed unexpectedly, attempting to reconnect...")
        else:
            print(f"Connection to {address} skipped initially")
    except Exception as e:
        print(f"Connection to {address} failed: {e}")

async def Peering():
    NetData = DB.GetNetworkData()
    PeerAddresses = list(NetData["Nodes"])
    tasks = [ClientHandler(uri) for uri in PeerAddresses]
    await asyncio.gather(*tasks)

async def MonitorConnections():
    while True:
        await Peering()
        await asyncio.sleep(1)  # Periksa koneksi setiap 30 detik

async def main():
    await MonitorConnections()