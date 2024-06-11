import socket
from Database import Repositories as DB
import asyncio
class NodeHandler:
    def __init__(self):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        self.address = DB.GetUserData("NodeAddress")
        self.IPAddr = IPAddr
    async def OpenConnection(self, ReceiverAddress:int):
        s = socket.socket()
        ReceiverIP = DB.GetNetworkData["Nodes"][ReceiverAddress]["IP"]
        s.connect(ReceiverIP,ReceiverAddress)
    
