import asyncio
import json
import sys
import threading
from datetime import datetime
from pytz import UTC

from tkinter import *

from app_help import Config_dynamic
from get_data import call_api
from format_data import format



loop = asyncio.get_event_loop()
def start_collection():
    # instrument_name = instrument_name.entry.get()
    global path
    path = f'data/{instrument_name.entry.get()}_{datetime.now(UTC).strftime("%y-%m-%d-%H-%M-%S")}.txt'
    msg = \
        {"jsonrpc": "2.0",
         "method": "public/subscribe",
         "id": 42,
         "params": {
             "channels": [f"ticker.{instrument_name.entry.get()}.raw"]}
         }

    loop.run_until_complete(call_api(json.dumps(msg),path))
    # asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))
def stop_collection():
    # path = f'data/{instrument_name.entry.get()}_{datetime.now(UTC).strftime("%y-%m-%d-%H-%M-%S")}.txt'
    format(path)
    sys.exit()

root = Tk()
root.title(f"Deribit Ticker Data Collection")
root.iconbitmap("Deribit.ico")
root.geometry('500x300')
instrument_name = Config_dynamic(
    root, "Instrument Name", default="ETH-PERPETUAL", row=0)



th = threading.Thread(target = start_collection)
th.setDaemon(True)
start_btn = Button(root, text="Start", command = th.start)
start_btn.grid(row=4, column=0)

stop_btn = Button(root, text="Stop and save to csv",command = stop_collection)
stop_btn.grid(row=4, column=1)


root.mainloop()
