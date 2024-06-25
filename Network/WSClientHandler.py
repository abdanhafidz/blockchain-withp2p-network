import asyncio
import websockets
from Database import Repositories as DB
from Controller import BlockReceiverController
import json, datetime

TIMEOUT = 10

connected_nodes_set = set()

async def ClientHandler(address):
    try:
        async with websockets.connect(f"ws://{address}:8333") as websocket:
            print(f"Connection to {address} succeeded")
            connected_nodes_set.add(address)  # Tandai bahwa node berhasil terkoneksi
            await websocket.send("ping")
            while True:
                message = await websocket.recv()
                
                if message != '':
                    ReceivedBlock = json.loads(json.dumps(message))
                    print("Block Received : ",ReceivedBlock)
                    BlockReceiverController.Control(ReceivedBlock)
        
    except asyncio.exceptions.TimeoutError:
        client_host = address
        NetData = DB.GetNetworkData()
        dict = {"IP":client_host,
            "LastChanged":str(datetime.datetime.now()),
            "Latency":NetData["Nodes"][client_host]["Latency"],
            "Status":"Offline"
            }
        DB.CreateNetworkData(client_host, dict)
    except websockets.exceptions.ConnectionClosedError:
        if address in connected_nodes_set:
            client_host = address
            NetData = DB.GetNetworkData()
            dict = {"IP":client_host,
            "LastChanged":str(datetime.datetime.now()),
            "Latency":NetData["Nodes"][client_host]["Latency"],
            "Status":"Offline"
            }
            DB.CreateNetworkData(client_host, dict)
            print(f"Connection to {address} closed unexpectedly, attempting to reconnect...")
        else:
            client_host = address
            NetData = DB.GetNetworkData()
            dict = {"IP":client_host,
            "LastChanged":str(datetime.datetime.now()),
            "Latency":NetData["Nodes"][client_host]["Latency"],
            "Status":"Offline"
            }
            DB.CreateNetworkData(client_host, dict)
            print(f"Connection to {address} skipped initially")
    except Exception as e:
        client_host = address
        NetData = DB.GetNetworkData()
        dict = {"IP":client_host,
        "LastChanged":str(datetime.datetime.now()),
        "Latency":NetData["Nodes"][client_host]["Latency"],
        "Status":"Offline"
        }
        DB.CreateNetworkData(client_host, dict)
        print(f"Connection to {address} failed: {e}")

async def Peering():
    NetData = DB.GetNetworkData()
    PeerAddresses = list(NetData["Nodes"])
    tasks = [ClientHandler(uri) for uri in PeerAddresses]
    await asyncio.gather(*tasks)

async def MonitorConnections():
    print("Client Network Panel : ")
    while True:
        await Peering()
        await asyncio.sleep(1)  # Periksa koneksi setiap 30 detik

async def main():
    await MonitorConnections()