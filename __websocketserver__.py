# from Socket import serve as Server
# from Socket import peer as Peer
from Network import WSServerHandler
import asyncio

asyncio.run(WSServerHandler.main())
