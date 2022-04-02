import pyupbit
import time
import uprank20_2 as rk
import pyupbase as pb

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

print("start")
a = 0
while a < 100:
    coin1_current_price = pyupbit.get_current_price(coin1)
    # coin2_current_price = pyupbit.get_current_price(coin2)
    # coin3_current_price = pyupbit.get_current_price(coin3)
    # coin4_current_price = pyupbit.get_current_price(coin4)
    # coin5_current_price = pyupbit.get_current_price(coin5)
    # coin6_current_price = pyupbit.get_current_price(coin6)
    # coin7_current_price = pyupbit.get_current_price(coin7)
    # coin8_current_price = pyupbit.get_current_price(coin8)
    # coin9_current_price = pyupbit.get_current_price(coin9)
    # coin10_current_price = pyupbit.get_current_price(coin10)
    # coin11_current_price = pyupbit.get_current_price(coin11)
    # coin12_current_price = pyupbit.get_current_price(coin12)
    # coin13_current_price = pyupbit.get_current_price(coin13)
    # coin14_current_price = pyupbit.get_current_price(coin14)
    # coin15_current_price = pyupbit.get_current_price(coin15)
    # coin16_current_price = pyupbit.get_current_price(coin16)
    # coin17_current_price = pyupbit.get_current_price(coin17)
    # coin18_current_price = pyupbit.get_current_price(coin18)
    # coin19_current_price = pyupbit.get_current_price(coin19)
    # coin20_current_price = pyupbit.get_current_price(coin20)

    print(coin1_current_price)
    # print(coin2_current_price)
    # print(coin3_current_price)
    # print(coin4_current_price)
    # print(coin5_current_price)
    # print(coin6_current_price)
    # print(coin7_current_price)
    # print(coin8_current_price)
    # print(coin9_current_price)
    # print(coin10_current_price)
    # print(coin11_current_price)
    # print(coin12_current_price)
    # print(coin13_current_price)
    # print(coin14_current_price)
    # print(coin15_current_price)
    # print(coin16_current_price)
    # print(coin17_current_price)
    # print(coin18_current_price)
    # print(coin19_current_price)
    # print(coin20_current_price)
    a = a + 1
    print(a)
    time.sleep(0.1)