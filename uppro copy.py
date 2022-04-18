# 2022 04 06 시작 From noneed/uppro3.py h>t -> h>=t 변경. 이유 : 백원대 코인들 하나 올라가면 1퍼씩 올라감.
#buy에 함수 빼고 그냥 지정변수로
#백테스트도 다시 해야겠는데
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

access_key = "a"
secret_key = "b"
upbit = pyupbit.Upbit(access_key, secret_key)

k = 0.5
target_v = 0.2
m = 10
amount = 20
base = '11h'
base_time = 11

def get_range(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = 72)
    y_day = df.iloc[-2]

    y_high = y_day['high']
    y_low = y_day['low']
    range = y_high - y_low
    return range

def get_open(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = 72)
    today = df.iloc[-1]
    open = today['open']
    return open

def get_y_open(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = 72)
    today = df.iloc[-2]
    open = today['open']
    return open

def get_percentage(ticker):
    range = get_range(ticker)
    y_open = get_y_open(ticker)
    range_ratio = range/y_open
    if target_v > range_ratio:
        percentage = 1/amount
    else:
        percentage = (1/amount)*(target_v/range_ratio)
    return percentage

def get_target_price(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = 72)
    today = df.iloc[-1]

    t_open = today['open']
    range = get_range(ticker)
    target_price = t_open + range * k
    if target_price <= 500:
        target_price = buyable(target_price)
    return target_price

def get_ma10(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = (m+1)*24)
    open = df['open']
    ma = open.rolling(window=m).mean()
    return ma[-1]

def buyable(ticker):
    price = get_target_price(ticker)
    # price = price * 1.002
    if price - 1 < 0:
        if price * 10 - 1 < 0:
            price = price * 10000
            if price != int(price):
                price = price + 1
            price = math.floor(price)
            price = price / 10000
        else:
            price = price * 1000
            price = math.floor(price)
            price = price + 1
            price = price / 1000
    elif len(str(math.floor(price))) == 1:
        price = price * 100
        price = math.floor(price)
        price = price + 1
        price = price / 100
    elif len(str(math.floor(price))) == 2:
        price = price * 10
        price = math.floor(price)
        price = price + 1
        price = price / 10
    elif len(str(math.floor(price))) == 3:
        price = math.floor(price)
        price = price + 1
    return price

def buy_market(ticker, krw, percentage):
    krw = krw * percentage
    upbit.buy_market_order(ticker, krw)

def sell_market(ticker, volume):#volume 가져와야함 -> 미리 지정
    upbit.sell_market_order(ticker, volume)
