from ctypes.wintypes import tagMSG
import pyupbit
import time
import datetime
import math

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)


def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    today = df.iloc[-1]

    t_open = today['open']
    range = get_range(ticker)
    k = 0.5
    target_price = t_open + range * k
    return target_price

def get_range(ticker):
    df = pyupbit.get_ohlcv(ticker, count=3)
    y_day = df.iloc[-2]

    y_high = y_day['high']
    y_low = y_day['low']
    range = y_high - y_low
    return range

def sell_price(ticker):
    price = pyupbit.get_current_price(ticker)
    price = price * 0.998
    return price

def sellable(ticker):
    price = sell_price(ticker)
    if price - 1 < 0:
        if price * 10 - 1 < 0:
            price = price * 10000
            price = math.floor(price)
            price = price - 1
            price = price / 10000
        else:
            price = price * 10000
            price = math.floor(price)
            price = price - 1
            price = price / 10000
    elif len(str(math.floor(price))) == 1:
        price = price * 100
        price = math.floor(price)
        price = price - 1
        price = price / 100
    elif len(str(math.floor(price))) == 2:
        price = price * 10
        price = math.floor(price)
        price = price / 10
    elif len(str(math.floor(price))) == 3:
        price = math.floor(price)
        price = price - 1
    elif len(str(math.floor(price))) == 4:
        if price % 10 <= 5: 
            price = price / 10
            price = math.floor(price)
            price = price * 10
        else:
            price = price / 10
            price = math.floor(price)
            price = price * 10
            price = price + 5
    elif len(str(math.floor(price))) == 5:
        price = price / 10
        price = math.floor(price)
        price = price * 10
    elif len(str(math.floor(price))) == 6:
        if (price/10) % 10 <= 5: 
            price = price / 100
            price = math.floor(price)
            price = price * 100
        else:
            price = price / 100
            price = math.floor(price)
            price = price * 100
            price = price + 50
    elif len(str(math.floor(price))) >=7:
        price = price / 1000
        price = math.floor(price)
        price = price * 1000
    return price

# tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-LTC"]


a = upbit.get_order("KRW-BTC")
for i in a:
    upbit.cancel_order(i['uuid'])