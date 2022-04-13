from re import L
import pyupbit
import asyncio
import datetime
import json

# now = datetime.datetime.now()
# a = pyupbit.get_current_price("KRW-BTC")
# b = pyupbit.get_current_price("KRW-ETH")
# c = pyupbit.get_current_price("KRW-XRP")
# print(a, b, c)
# end = datetime.datetime.now()
# print(end-now)

now = datetime.datetime.now()
async def a():
    print("1 s")
    a = pyupbit.get_current_price("KRW-BTC")
    print("1 e")
    # print("a started")
    # await asyncio.sleep(3)
    # a = 3 
    # print("a ended")
    return(a)
async def b():
    print("2 s")
    a = pyupbit.get_current_price("KRW-ETH")
    print("2 e")
    # print("b started")
    # await asyncio.sleep(2)
    # a = 4
    # print("b ended")
    return(a)
async def c():
    print("3 s")
    a = pyupbit.get_current_price("KRW-XRP")
    print("3 e")
    # print("c started")
    # await asyncio.sleep(1)
    # a = 5
    # print("c ended")
    return(a)
async def main():
    ab = a()
    bb = b()
    cb = c()
    result = await asyncio.gather(ab,bb,cb)
    return result
print("main start")
asyncio.run(main())
print("main end")
end = datetime.datetime.now()
print(end-now)