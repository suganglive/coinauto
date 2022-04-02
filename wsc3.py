from re import sub
import websockets
import asyncio
import json
import time
import datetime
import logging

logging.basicConfig(filename='uppro.log', level=logging.INFO, format='%(asctime)s:%(message)s')

coin1 = "KRW-BTC"
coin2 = "KRW-ETH"
coin3 = "KRW-XRP"
coin4 = "KRW-LTC"
coin5 = "KRW-ZIL"
coin6 = "KRW-TT"
coin7 = "KRW-WAVES"
coin8 = "KRW-AAVE"
coin9 = "KRW-AXS"
coin10 = "KRW-POWR"
coin11 = "KRW-SOL"
coin12 = "KRW-UPP"
coin13 = "KRW-RFR"
coin14 = "KRW-NED"
coin15 = "KRW-SAND"
coin16 = "KRW-ETC"
coin17 = "KRW-FLOW"
coin18 = "KRW-MOC"
coin19 = "KRW-MVL"
coin20 = "KRW-SRM"

# now = datetime.datetime.now()
# end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=11, minutes=32)

# if now > end:
#     end = end + datetime.timedelta(1)
# a = "hi"


async def program():
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [{"ticket":"test"}, {"type":"ticker", "codes":[coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20], "isOnlyRealtime": True}, {"format":"SIMPLE"}]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        now = datetime.datetime.now()
        end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=23, minutes=1)

        if now > end:
            end = end + datetime.timedelta(1)

        while True:
            now = datetime.datetime.now()
            logging.info(a)
            if end < now:
                break
            data = await websocket.recv()
            data = json.loads(data)
            # logging.info(data['cd'], data['tp'])
            if data['cd'] == coin1:
                logging.info(coin1, data['tp'])
            elif data['cd'] == coin2:
                logging.info(coin2, data['tp'])
            elif data['cd'] == coin3:
                logging.info(coin3, data['tp'])
            elif data['cd'] == coin4:
                logging.info(coin4, data['tp'])
            elif data['cd'] == coin5:
                logging.info(coin5, data['tp'])
            elif data['cd'] == coin6:
                logging.info(coin6, data['tp'])
            elif data['cd'] == coin7:
                logging.info(coin7, data['tp'])
            elif data['cd'] == coin8:
                logging.info(coin8, data['tp'])
            elif data['cd'] == coin9:
                logging.info(coin9, data['tp'])
            elif data['cd'] == coin10:
                logging.info(coin10, data['tp'])
            elif data['cd'] == coin11:
                logging.info(coin11, data['tp'])
            elif data['cd'] == coin12:
                logging.info(coin12, data['tp'])
            elif data['cd'] == coin13:
                logging.info(coin13, data['tp'])
            elif data['cd'] == coin14:
                logging.info(coin14, data['tp'])
            elif data['cd'] == coin15:
                logging.info(coin15, data['tp'])
            elif data['cd'] == coin16:
                logging.info(coin16, data['tp'])
            elif data['cd'] == coin17:
                logging.info(coin17, data['tp'])
            elif data['cd'] == coin18:
                logging.info(coin18, data['tp'])
            elif data['cd'] == coin19:
                logging.info(coin19, data['tp'])
            elif data['cd'] == coin20:
                logging.info(coin20, data['tp'])
            
async def main():
    await program()
logging.info("stage 0")
asyncio.run(main())
# logging.info("hi")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

# async def bithumb_ws_client():
#     uri = "wss://pubwss.bithumb.com/pub/ws"

#     async with websockets.connect(uri, ping_interval = None) as websocket:
#         greeting = await websocket.recv()
#         logging.info(greeting)

#         subscribe_fmt = {"type":"ticker", "symbols": ["BTC_KRW"], "tickTypes": ["1H"]}
#         subscribe_data = json.dumps(subscribe_fmt)
#         await websocket.send(subscribe_data)

#         while True:
#             data = await websocket.recv()
#             data = json.loads(data)
#             logging.info(data)

# async def main():
#     await bithumb_ws_client()

# asyncio.run(main())
