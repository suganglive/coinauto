import pyupbit
import time
import datetime
import math

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

# def get_current_price(ticker):
#     df = pyupbit.get_current_price(ticker)
#     return df

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    y_day = df.iloc[-2]
    today = df.iloc[-1]

    t_open = today['open']
    y_high = y_day['high']
    y_low = y_day['low']
    k = 0.5
    target_price = t_open + (y_high - y_low) * k
    return target_price

def get_open(ticker):
    df = pyupbit.get_ohlcv(ticker)
    today = df.iloc[-1]
    open = today['open']
    return open

def get_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker)
    open = df['open']
    ma = open.rolling(window=5).mean()
    return ma[-1]

def buyable_btc(ticker):
    btc_current_price = pyupbit.get_current_price(ticker)
    btc_price = btc_current_price * 1.002
    btc_price = btc_price/1000
    btc_price = math.ceil(btc_price)
    btc_price = btc_price * 1000
    return btc_price

def buy_limit(ticker):
    # krw = upbit.get_balance("KRW")
    krw = 2000000
    btc_price = buyable_btc("KRW-BTC")
    unit = krw/float(btc_price)
    upbit.buy_limit_order(ticker, btc_price, unit)

def sellable_btc(ticker):
    btc_current_price = pyupbit.get_current_price(ticker)
    btc_price = btc_current_price * 0.998
    btc_price = btc_price/1000
    btc_price = math.ceil(btc_price)
    btc_price = btc_price * 1000
    return btc_price

def sell_limit(ticker):
    unit = upbit.get_balance(ticker)
    btc_price = sellable_btc("KRW-" + ticker)
    upbit.sell_limit_order("KRW-" + ticker, btc_price, unit)

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_ma5("KRW-BTC")
target_price = get_target_price("KRW-BTC")
btc_status = 0

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_ma5("KRW-BTC")
            sell_limit("BTC")
            btc_status = 0
        
        current_price = pyupbit.get_current_price("KRW-BTC")
        open_price = get_open("KRW-BTC")
        if current_price > target_price and btc_status == 0 and open_price > ma5:
            buy_limit("KRW-BTC")
            btc_status = 1
        # print("current_price : ", current_price)
        # print("target_price : ", target_price)
        # print("btc_status : ", btc_status)
        # print("open_price : ", open_price)
        # print("ma5 : ", ma5)

    except:
        print("에러 발생")
    time.sleep(1)
