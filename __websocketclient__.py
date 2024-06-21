# from Socket import serve as Server
# from Socket import peer as Peer
from Network import WSClientHandler
import asyncio

asyncio.run(WSClientHandler.main())
