import asyncio
import pyupbit
import datetime
# from datetime import timedelta
import uprank20_2 as rk

tickers = rk.get_tickers(base = '11h')
coin1 = tickers[0]
coin2 = tickers[1]
coin3 = tickers[2]
coin4 = tickers[3]
coin5 = tickers[4]
coin6 = tickers[5]
coin7 = tickers[6]
coin8 = tickers[7]
coin9 = tickers[8]
coin10 = tickers[9]
coin11 = tickers[10]
coin12 = tickers[11]
coin13 = tickers[12]
coin14 = tickers[13]
coin15 = tickers[14]
coin16 = tickers[15]
coin17 = tickers[16]
coin18 = tickers[17]
coin19 = tickers[18]
coin20 = tickers[19]

now= datetime.datetime.now()
coin1_current_price = pyupbit.get_current_price(coin1)
coin2_current_price = pyupbit.get_current_price(coin2)
coin3_current_price = pyupbit.get_current_price(coin3)
coin4_current_price = pyupbit.get_current_price(coin4)
coin5_current_price = pyupbit.get_current_price(coin5)
coin6_current_price = pyupbit.get_current_price(coin6)
coin7_current_price = pyupbit.get_current_price(coin7)
coin8_current_price = pyupbit.get_current_price(coin8)
coin9_current_price = pyupbit.get_current_price(coin9)
coin10_current_price = pyupbit.get_current_price(coin10)
coin11_current_price = pyupbit.get_current_price(coin11)
coin12_current_price = pyupbit.get_current_price(coin12)
coin13_current_price = pyupbit.get_current_price(coin13)
coin14_current_price = pyupbit.get_current_price(coin14)
coin15_current_price = pyupbit.get_current_price(coin15)
coin16_current_price = pyupbit.get_current_price(coin16)
coin17_current_price = pyupbit.get_current_price(coin17)
coin18_current_price = pyupbit.get_current_price(coin18)
coin19_current_price = pyupbit.get_current_price(coin19)
coin20_current_price = pyupbit.get_current_price(coin20)
# print("hi")
end= datetime.datetime.now()
print(end-now)

now= datetime.datetime.now()
async def c1():
    coin1_current_price = pyupbit.get_current_price(coin1)
    return coin1_current_price
async def c2():
    coin2_current_price = pyupbit.get_current_price(coin2)
    return coin2_current_price
async def c3():
    coin3_current_price = pyupbit.get_current_price(coin3)
    return coin3_current_price
async def c4():
    coin4_current_price = pyupbit.get_current_price(coin4)
    return coin4_current_price
async def c5():
    coin5_current_price = pyupbit.get_current_price(coin5)
    return coin5_current_price
async def c6():
    coin6_current_price = pyupbit.get_current_price(coin6)
    return coin6_current_price
async def c7():
    coin7_current_price = pyupbit.get_current_price(coin7)
    return coin7_current_price
async def c8():
    coin8_current_price = pyupbit.get_current_price(coin8)
    return coin8_current_price
async def c9():
    coin9_current_price = pyupbit.get_current_price(coin9)
    return coin9_current_price
async def c10():
    coin10_current_price = pyupbit.get_current_price(coin10)
    return coin10_current_price
async def c11():
    coin11_current_price = pyupbit.get_current_price(coin11)
    return coin11_current_price
async def c12():
    coin12_current_price = pyupbit.get_current_price(coin12)
    return coin12_current_price
async def c13():
    coin13_current_price = pyupbit.get_current_price(coin13)
    return coin13_current_price
async def c14():
    coin14_current_price = pyupbit.get_current_price(coin14)
    return coin14_current_price
async def c15():
    coin15_current_price = pyupbit.get_current_price(coin15)
    return coin15_current_price
async def c16():
    coin16_current_price = pyupbit.get_current_price(coin16)
    return coin16_current_price
async def c17():
    coin17_current_price = pyupbit.get_current_price(coin17)
    return coin17_current_price
async def c18():
    coin18_current_price = pyupbit.get_current_price(coin18)
    return coin18_current_price
async def c19():
    coin19_current_price = pyupbit.get_current_price(coin19)
    return coin19_current_price
async def c20():
    coin20_current_price = pyupbit.get_current_price(coin20)
    return coin20_current_price
    
async def main():
    # try:
    co1 = c1()
    co2 = c2()
    co3 = c3()
    co4 = c4()
    co5 = c5()
    co6 = c6()
    co7 = c7()
    co8 = c8()
    co9 = c9()
    co10 = c10()
    co11 = c11()
    co12 = c12()
    co13 = c13()
    co14 = c14()
    co15 = c15()
    co16 = c16()
    co17 = c17()
    co18 = c18()
    co19 = c19()
    co20 = c20()

    result = await asyncio.gather(co1, co2, co3, co4, co5, co6, co7, co8, co9, co10, co11, co12, co13, co14, co15, co16, co17, co18, co19, co20)
    # result = await asyncio.gather(co1, co2, co3, co4, co5)
    # result = await asyncio.gather(co1, co2)
    # except Exception as e:
    #     print(e)
    #     pass
    return result

cp = list(asyncio.run(main()))
print(cp)
end= datetime.datetime.now()
print(end-now)
# coin1_current_price = cp[0]
# coin2_current_price = cp[1]
# coin3_current_price = cp[2]
# coin4_current_price = cp[3]
# coin5_current_price = cp[4]
# coin6_current_price = cp[5]
# coin7_current_price = cp[6]
# coin8_current_price = cp[7]
# coin9_current_price = cp[8]
# coin10_current_price = cp[9]
# coin11_current_price = cp[10]
# coin12_current_price = cp[11]
# coin13_current_price = cp[12]
# coin14_current_price = cp[13]
# coin15_current_price = cp[14]
# coin16_current_price = cp[15]
# coin17_current_price = cp[16]
# coin18_current_price = cp[17]
# coin19_current_price = cp[18]
# coin20_current_price = cp[19]
# print("hi", coin1_current_price, coin2_current_price)
# coin1 = "KRW-BTC-BTC"
# coin2 = "KRW-BTC-XRP"

# async def a():
#     a = pyupbit.get_current_price(coin1)
#     # print(a)
#     return a



# async def b():
#     b = pyupbit.get_current_price(coin2)
#     # print(b)
#     return b

# async def main():
#     zz = a()
#     xx = b()
#     result = await asyncio.gather(zz,xx)
#     print(result)
#     return result
#     # print(result)#리스트로 반환하는구나 asyncio.gather

# print("Main Start")
# result = list(asyncio.run(main()))
# print(result[0])
# print("Main End")

# loop = asyncio.get_event_loop()
# result = list(loop.run_until_complete(main()))
# print(result[0])
# loop.close()

