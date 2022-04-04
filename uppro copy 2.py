import websockets
import asyncio
import json
import pyupbit
import time
import datetime
import logging
import pyupbase as pb
import uprank20_2 as rk
import math

logging.basicConfig(filename='uppro.log', level=logging.INFO, format='%(asctime)s:%(message)s')

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[1].strip()
    secret_key = lines[2].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

a = 123

async def upbit_ws_client(callback):
    uri = 'wss://api.upbit.com/websocket/v1'
    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [{'ticket':'test'}, {'type':'ticker', 'codes':['KRW-BTC'], 'isOnlyRealtime':True}, {'format':'SIMPLE'},
        {'ticket':'test'}, {'type':'ticker', 'codes':['KRW-XRP'], 'isOnlyRealtime':True}, {'format':'SIMPLE'}]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            await callback(await websocket.recv())


async def response_message(*args, **kwargs):
    print(args, a)

if __name__ == '__main__':
    tasks = [asyncio.ensure_future(upbit_ws_client(response_message))]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
