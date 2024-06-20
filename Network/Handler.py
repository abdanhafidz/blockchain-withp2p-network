import socket
from Database import Repositories as DB
from Models.Interface import Block
import asyncio
class NodeHandler:
    def __init__(self):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        self.address = DB.GetUserData("NodeAddress")
        self.IPAddr = IPAddr
        self.port = 8333
    async def Listen(self, ReceiverAddress:int):
        s = socket.socket()
        port = self.port
        s.connect(ReceiverAddress,port)
        while True:
            res = s.recv(2048).decode()
        return res

    async def Brodcast(self, data:Block):
        s = socket.socket()            
        s.bind(('', self.port))         
        print ("Socket binded to %s" %(self.port)) 
        s.listen(5)     
        print ("socket is listening")            
        while True: 
            c, addr = await s.accept()     
            if(not DB.GetNetworkData["Nodes"]):
                dict = {
                    "{addr}" : {
                    "IP":addr,
                    "LastChanged":""
                    }
                }
            DB.CreateNetworkData(dict)
            print ('Got connection from', addr)
            c.send(data.__dict__.encode('utf-8')) 
            break

    
