# 바이낸스, 상승장, 변동성 돌파, 변동성 조절 Coins : [BTC, ETH, XRP, LTC]
import ccxt
import time
import datetime
from datetime import datetime
import math
import logging
import pandas as pd

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[2].strip()
    secret_key = lines[3].strip()
    binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

# access_key = lines[2].strip()
# secret_key = lines[3].strip()
# binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

tickers = ["BTC/USDT", "ETH/USDT", "XRP/USDT", "LTC/USDT"]

# ohlcs = binance.fetch_ohlcv(tickers[0], timeframe='1d') 
# print(ohlcs)
# for i in ohlcs:
#     print(datetime.fromtimestamp(i[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), i)
# print(ohlcs[-1][4])

def get_range(ticker):
    # df = pyupbit.get_ohlcv(ticker, count=3)
    df = binance.fetch_ohlcv(ticker, timeframe='1d')
    y_day = df[-2]

    y_high = y_day[2]
    y_low = y_day[3]
    range = y_high - y_low
    range = round(range, 2)
    return range

def get_y_open(ticker):
    df = binance.fetch_ohlcv(ticker, timeframe='1d')
    today = df[-2]
    open = today[1]
    return open

def get_percentage(ticker):
    range = get_range(ticker)
    y_open = get_y_open(ticker)
    target_v = 0.05
    range_ratio = range/y_open
    if target_v > range_ratio:
        percentage = 1/4
    else:
        percentage = (1/4)*(target_v/range_ratio)
    return percentage

def get_target_price(ticker):
    df = binance.fetch_ohlcv(ticker, timeframe='1d')
    today = df[-1]

    t_open = today[1]
    range = get_range(ticker)
    k = 0.5
    target_price = t_open + range * k
    return target_price

def get_open(ticker):
    df = binance.fetch_ohlcv(ticker, timeframe='1d')
    today = df[-1]
    open = today[1]
    return open

def get_ma5(ticker):
    df = binance.fetch_ohlcv(ticker, timeframe='1d')
    header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = pd.DataFrame(df, columns=header)
    open = df['Open']
    ma = open.rolling(window=5).mean()
    ma = float(ma.iloc[-1])
    return ma

print(get_ma5(tickers[0]))
print(type(get_ma5(tickers[0])))



