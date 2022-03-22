import pyupbit
import time
import datetime
import logging
import pyupbase as pb
import uprank20 as rk

m = 10
ticker = "KRW-BTC"

def get_ma10(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, count = m*24 + 5)
    open = df['open']
    ma = open.rolling(window=m).mean()
    return ma[-1]

a = get_ma10(ticker = ticker)
print(a)

print(pb.get_daily_ohlcv_from_base("KRW-BTC", base ='10h', count=240))
