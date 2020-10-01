import asyncio
import collections
import json
from datetime import datetime
from pprint import pprint

import websockets
from pytz import UTC

# To subscribe to this channel:
# msg = \
#     {"jsonrpc": "2.0",
#      "method": "public/subscribe",
#      "id": 42,
#      "params": {
#          "channels": ["ticker.ETH-PERPETUAL.raw"]}
#      }




async def call_api(msg,path):
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(msg)
        await websocket.recv()
        print("The program is collecting data")
        print(f"path : {path}")
        with open(path, "w") as f:           
            while websocket.open:
                response = await websocket.recv()
                f.write(f"{response}\n")

# asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg,path)))
