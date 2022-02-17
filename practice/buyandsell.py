from decimal import ROUND_CEILING, ROUND_UP
import pyupbit
import time
import datetime
import math

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

# now = datetime.datetime.now()
# nine = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=11,minutes=25)
# print(now)
# print(nine)
# nine = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=11,minutes=30)
# print(nine)

# while True:
#     now = datetime.datetime.now()
#     if nine < now < nine + datetime.timedelta(seconds=10):
#         nine = nine + datetime.timedelta(1)
#         print(nine)
#         print("It's time")
#     else:
#         print("not yet")
#     time.sleep(1)

def get_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker)
    open = df['open']
    ma = open.rolling(window=5).mean()
    return ma[-1]

# print(get_ma5("KRW-BTC"))
print(type(pyupbit.get_ohlcv("KRW-BTC")))