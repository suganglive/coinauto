# 업비트, 상승장, 변동성 돌파, 변동성 조절 Coins : [BTC, ETH, XRP, LTC], 9시 초기화
import pyupbit
import time
import datetime
import math

access_key = "a"
secret_key = "b"
upbit = pyupbit.Upbit(access_key, secret_key)

def get_range(ticker):
    df = pyupbit.get_ohlcv(ticker, count=3)
    y_day = df.iloc[-2]

    y_high = y_day['high']
    y_low = y_day['low']
    range = y_high - y_low
    return range

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
    df = pyupbit.get_ohlcv(ticker)
    today = df.iloc[-1]

    t_open = today['open']
    range = get_range(ticker)
    k = 0.5
    target_price = t_open + range * k
    return target_price

def get_open(ticker):
    df = pyupbit.get_ohlcv(ticker)
    today = df.iloc[-1]
    open = today['open']
    return open

def get_y_open(ticker):
    df = pyupbit.get_ohlcv(ticker)
    today = df.iloc[-2]
    open = today['open']
    return open

def get_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker)
    open = df['open']
    ma = open.rolling(window=5).mean()
    return ma[-1]

def buyable():
    btc_current_price = pyupbit.get_current_price("KRW-BTC")
    btc_price = btc_current_price * 1.002
    btc_price = btc_price/1000
    btc_price = math.ceil(btc_price)
    btc_price = btc_price * 1000

    eth_current_price = pyupbit.get_current_price("KRW-ETH")
    eth_price = eth_current_price * 1.002
    eth_price = eth_price/1000
    eth_price = math.ceil(eth_price)
    eth_price = eth_price * 1000

    xrp_orderbook = pyupbit.get_orderbook("KRW-XRP")
    xrp_price = xrp_orderbook["orderbook_units"][0]['ask_price']

    ltc_orderbook = pyupbit.get_orderbook("KRW-LTC")
    ltc_price = ltc_orderbook["orderbook_units"][0]['ask_price']

    return btc_price, eth_price, xrp_price, ltc_price

def buy_btc():
    percentage = get_percentage("KRW-BTC")
    krw = krw * percentage
    btc_price = buyable()[0]
    unit = krw/float(btc_price)
    upbit.buy_limit_order("KRW-BTC", btc_price, unit)

def buy_eth():
    percentage = get_percentage("KRW-ETH")
    krw = krw * percentage
    eth_price = buyable()[1]
    unit = krw/float(eth_price)
    upbit.buy_limit_order("KRW-ETH", eth_price, unit)

def buy_xrp():
    percentage = get_percentage("KRW-XRP")
    krw = krw * percentage
    xrp_price = buyable()[2]
    unit = krw/float(xrp_price)
    upbit.buy_limit_order("KRW-XRP", xrp_price, unit)

def buy_ltc():
    percentage = get_percentage("KRW-LTC")
    krw = krw * percentage
    ltc_price = buyable()[3]
    unit = krw/float(ltc_price)
    upbit.buy_limit_order("KRW-LTC", ltc_price, unit)

def sellable():
    btc_current_price = pyupbit.get_current_price("KRW-BTC")
    btc_price = btc_current_price * 0.998
    btc_price = btc_price/1000
    btc_price = math.ceil(btc_price)
    btc_price = btc_price * 1000

    eth_current_price = pyupbit.get_current_price("KRW-ETH")
    eth_price = eth_current_price * 0.998
    eth_price = eth_price/1000
    eth_price = math.ceil(eth_price)
    eth_price = eth_price * 1000

    xrp_orderbook = pyupbit.get_orderbook("KRW-XRP")
    xrp_price = xrp_orderbook["orderbook_units"][0]['bid_price']

    ltc_orderbook = pyupbit.get_orderbook("KRW-LTC")
    ltc_price = ltc_orderbook["orderbook_units"][0]['bid_price']

    return btc_price, eth_price, xrp_price, ltc_price

def sell_limit():
    btc_unit = upbit.get_balance("BTC")
    btc_price = sellable()[0]
    upbit.sell_limit_order("KRW-BTC", btc_price, btc_unit)

    eth_unit = upbit.get_balance("ETH")
    eth_price = sellable()[1]
    upbit.sell_limit_order("KRW-ETH", eth_price, eth_unit)

    xrp_unit = upbit.get_balance("XRP")
    xrp_price = sellable()[2]
    upbit.sell_limit_order("KRW-XRP", xrp_price, xrp_unit)

    ltc_unit = upbit.get_balance("LTC")
    ltc_price = sellable()[3]
    upbit.sell_limit_order("KRW-LTC", ltc_price, ltc_unit)

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=8, minutes=59)

if now > mid:
    mid = mid + datetime.timedelta(1)

a = 0
while a == 0:
    try:
        btc_open = get_open("KRW-BTC")
        btc_ma5 = get_ma5("KRW-BTC")
        btc_target = get_target_price("KRW-BTC")
        btc_status = 0

        eth_open = get_open("KRW-ETH")
        eth_ma5 = get_ma5("KRW-ETH")
        eth_target = get_target_price("KRW-ETH")
        eth_status = 0

        xrp_open = get_open("KRW-XRP")
        xrp_ma5 = get_ma5("KRW-XRP")
        xrp_target = get_target_price("KRW-XRP")
        xrp_status = 0

        ltc_open = get_open("KRW-LTC")
        ltc_ma5 = get_ma5("KRW-LTC")
        ltc_target = get_target_price("KRW-LTC")
        ltc_status = 0

        krw = upbit.get_balance("KRW")
        a = 1
    except:
        print("기본 값 오류")
        time.sleep(10)

print("프로그램 가동 중...")
while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10):
            btc_target = get_target_price("KRW-BTC")
            eth_target = get_target_price("KRW-ETH")
            xrp_target = get_target_price("KRW-XRP")
            ltc_target = get_target_price("KRW-LTC")
            btc_ma5 = get_ma5("KRW-BTC")
            eth_ma5 = get_ma5("KRW-ETH")
            xrp_ma5 = get_ma5("KRW-XRP")
            ltc_ma5 = get_ma5("KRW-LTC")
            sell_limit()
            btc_status = 0
            eth_status = 0
            xrp_status = 0
            ltc_status = 0
            krw = upbit.get_balance("KRW")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

        btc_current_price = pyupbit.get_current_price("KRW-BTC")
        eth_current_price = pyupbit.get_current_price("KRW-ETH")
        xrp_current_price = pyupbit.get_current_price("KRW-XRP")
        ltc_current_price = pyupbit.get_current_price("KRW-LTC")
        btc_open = get_open("KRW-BTC")
        eth_open = get_open("KRW-ETH")
        xrp_open = get_open("KRW-XRP")
        ltc_open = get_open("KRW-LTC")
        if btc_current_price > btc_target and btc_status == 0 and btc_open > btc_ma5:
            buy_btc()
            btc_status = 1

        if eth_current_price > eth_target and eth_status == 0 and eth_open > eth_ma5:
            buy_eth()
            eth_status = 1

        if xrp_current_price > xrp_target and xrp_status == 0 and xrp_open > xrp_ma5:
            buy_xrp()
            xrp_status = 1

        if ltc_current_price > ltc_target and ltc_status == 0 and ltc_open > ltc_ma5:
            buy_ltc()
            ltc_status = 1

    except:
        print("에러 발생")
    time.sleep(1)