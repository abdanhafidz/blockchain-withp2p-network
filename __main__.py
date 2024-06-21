# from Socket import serve as Server
# from Socket import peer as Peer
from Middleware import BlockChainSync

from Loader import Loader
try:
    print("Synchronize The BlockChain")
    BlockChainSync.SynchronizeBlockChain()
    Loader.LoadView(0)
except:
    print("Make Sure that You are Connected to the Internet!")
    

