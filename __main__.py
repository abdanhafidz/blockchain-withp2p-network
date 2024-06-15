# from Socket import serve as Server
# from Socket import peer as Peer
from Loader import Loader
from Network import WebSocket
import asyncio
if __name__ == "__main__":
    asyncio.run(WebSocket.main())
    Loader.LoadView(0)