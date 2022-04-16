import asyncio
import websockets
import json

async def upbit_ws_client(callback):
    uri = 'wss://api.upbit.com/websocket/v1'
    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {'ticket': 'test'},
            {
                'type': 'ticker',
                'codes': ['KRW-XRP'],
                'isOnlyRealtime': True
            },
            {
                'type': 'ticker',
                'codes': ['KRW-BTC'],
                'isOnlyRealtime': True
            },
            {'format': 'SIMPLE'}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            print('111111111')
            await callback(await websocket.recv())

# async def upbit_ws_client2(callback):
#     uri = 'wss://api.upbit.com/websocket/v1'
#     async with websockets.connect(uri) as websocket:
#         subscribe_fmt = [
#             {'ticket': 'test'},
#             {
#                 'type': 'ticker',
#                 'codes': ['KRW-XRP'],
#                 'isOnlyRealtime': True
#             },
#             {'format': 'SIMPLE'}
#         ]
#         subscribe_data = json.dumps(subscribe_fmt)
#         await websocket.send(subscribe_data)

#         while True:
#             print('2222222222')
#             await callback(await websocket.recv())

async def response_message(*args, **kwargs):
    print(args)

if __name__ == '__main__':
    tasks = [
        asyncio.ensure_future(upbit_ws_client(response_message))
        # asyncio.ensure_future(upbit_ws_client2(response_message))
    ]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
