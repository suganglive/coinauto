from re import sub
import websockets
import asyncio
import json
import time
import datetime

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

now = datetime.datetime.now()
end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=11, minutes=32)

if now > end:
    end = end + datetime.timedelta(1)
a = "hi"


async def program():
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [{"ticket":"test"}, {"type":"ticker", "codes":[coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20], "isOnlyRealtime": True}, {"format":"SIMPLE"}]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        now = datetime.datetime.now()
        end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=22, minutes=41)

        if now > end:
            end = end + datetime.timedelta(1)

        while True:
            now = datetime.datetime.now()
            print(a)
            if end < now:
                break
            data = await websocket.recv()
            data = json.loads(data)
            # print(data['cd'], data['tp'])
            if data['cd'] == coin1:
                print(coin1, data['tp'])
            elif data['cd'] == coin2:
                print(coin2, data['tp'])
            elif data['cd'] == coin3:
                print(coin3, data['tp'])
            elif data['cd'] == coin4:
                print(coin4, data['tp'])
            elif data['cd'] == coin5:
                print(coin5, data['tp'])
            elif data['cd'] == coin6:
                print(coin6, data['tp'])
            elif data['cd'] == coin7:
                print(coin7, data['tp'])
            elif data['cd'] == coin8:
                print(coin8, data['tp'])
            elif data['cd'] == coin9:
                print(coin9, data['tp'])
            elif data['cd'] == coin10:
                print(coin10, data['tp'])
            elif data['cd'] == coin11:
                print(coin11, data['tp'])
            elif data['cd'] == coin12:
                print(coin12, data['tp'])
            elif data['cd'] == coin13:
                print(coin13, data['tp'])
            elif data['cd'] == coin14:
                print(coin14, data['tp'])
            elif data['cd'] == coin15:
                print(coin15, data['tp'])
            elif data['cd'] == coin16:
                print(coin16, data['tp'])
            elif data['cd'] == coin17:
                print(coin17, data['tp'])
            elif data['cd'] == coin18:
                print(coin18, data['tp'])
            elif data['cd'] == coin19:
                print(coin19, data['tp'])
            elif data['cd'] == coin20:
                print(coin20, data['tp'])
            
async def main():
    await program()

# asyncio.run(main())
# print("hi")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# async def bithumb_ws_client():
#     uri = "wss://pubwss.bithumb.com/pub/ws"

#     async with websockets.connect(uri, ping_interval = None) as websocket:
#         greeting = await websocket.recv()
#         print(greeting)

#         subscribe_fmt = {"type":"ticker", "symbols": ["BTC_KRW"], "tickTypes": ["1H"]}
#         subscribe_data = json.dumps(subscribe_fmt)
#         await websocket.send(subscribe_data)

#         while True:
#             data = await websocket.recv()
#             data = json.loads(data)
#             print(data)

# async def main():
#     await bithumb_ws_client()

# asyncio.run(main())
