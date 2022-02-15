import pyupbit
import time
import datetime

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    y_high = yesterday['high']
    y_low = yesterday['low']
    k = 0.5
    target = today_open + (y_high - y_low) * k
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("KRW-BTC")

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10):
        target_price = get_target_price("KRW-BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    
    current_price = pyupbit.get_current_price("KRW-BTC")
    print(current_price)
    
    time.sleep(1)

