# 바이낸스, 상승장, 변동성 돌파, 변동성 조절 Coins : [BTC, ETH, XRP, LTC]
# nohup python3 mark3.py > output.log &
import ccxt
import time
import datetime
import math
import logging
import pandas as pd

logging.basicConfig(filename='mark3-1.log', level=logging.INFO, format='%(asctime)s:%(message)s')

# access_key = "a"
# secret_key = "b"
# binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[2].strip()
    secret_key = lines[3].strip()
    binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

tickers = ["BTC/USDT", "ETH/USDT", "XRP/USDT", "LTC/USDT"]

def get_range(ticker):
    df = binance.fetch_ohlcv(ticker, timeframe='1d')
    y_day = df[-2]

    y_high = y_day[2]
    y_low = y_day[3]
    range = y_high - y_low
    range = round(range, 3)
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

def buyable():
    btc_price = get_target_price("BTC/USDT")
    btc_price = btc_price * 1.002
    btc_price = btc_price * 100
    btc_price = math.floor(btc_price)
    btc_price = btc_price + 1
    btc_price = btc_price / 100

    eth_price = binance._price("ETH/USDT")
    eth_price = eth_price * 1.002
    eth_price = eth_price * 100
    eth_price = math.floor(eth_price)
    eth_price = eth_price + 1
    eth_price = eth_price / 100

    xrp_price = binance._price("XRP/USDT")
    xrp_price = xrp_price * 1.002
    xrp_price = xrp_price * 10000
    xrp_price = math.floor(xrp_price)
    xrp_price = xrp_price + 1
    xrp_price = xrp_price / 10000

    ltc_price = binance._price("LTC/USDT")
    ltc_price = ltc_price * 1.002
    ltc_price = ltc_price * 10
    ltc_price = math.floor(ltc_price)
    ltc_price = ltc_price + 1
    ltc_price = ltc_price / 10

    return btc_price, eth_price, xrp_price, ltc_price

def buy_btc():
    percentage = get_percentage("BTC/USDT")
    balance = balance * percentage
    btc_price = buyable()[0]
    unit = balance/float(btc_price)
    binance.create_limit_buy_order("BTC/USDT", unit, btc_price)

def buy_eth():
    percentage = get_percentage("ETH/USDT")
    balance = balance * percentage
    eth_price = buyable()[1]
    unit = balance/float(eth_price)
    binance.create_limit_buy_order("ETH/USDT",unit ,eth_price)

def buy_xrp():
    percentage = get_percentage("XRP/USDT")
    balance = balance * percentage
    xrp_price = buyable()[2]
    unit = balance/float(xrp_price)
    binance.create_limit_buy_order("XRP/USDT",unit, xrp_price)

def buy_ltc():
    percentage = get_percentage("LTC/USDT")
    balance = balance * percentage
    ltc_price = buyable()[3]
    unit = balance/float(ltc_price)
    binance.create_limit_buy_order("LTC/USDT",unit, ltc_price)

def sellable():
    btc_price = binance.fetch_ticker("BTC/USDT")
    btc_price = btc_price['close']
    btc_price = btc_price * 0.998
    btc_price = btc_price * 100
    btc_price = math.floor(btc_price)
    btc_price = btc_price - 1
    btc_price = btc_price / 100

    eth_price = binance.fetch_ticker("ETH/USDT")
    eth_price = eth_price['close']
    eth_price = eth_price * 0.998
    eth_price = eth_price * 100
    eth_price = math.floor(eth_price)
    eth_price = eth_price - 1
    eth_price = eth_price / 100

    xrp_price = binance.fetch_ticker("XRP/USDT")
    xrp_price = xrp_price['close']
    xrp_price = xrp_price * 0.998
    xrp_price = xrp_price * 10000
    xrp_price = math.floor(xrp_price)
    xrp_price = xrp_price - 1
    xrp_price = xrp_price / 10000

    ltc_price = binance.fetch_ticker("LTC/USDT")
    ltc_price = ltc_price['close']
    ltc_price = ltc_price * 0.998
    ltc_price = ltc_price * 10
    ltc_price = math.floor(ltc_price)
    ltc_price = ltc_price - 1
    ltc_price = ltc_price / 10

    return btc_price, eth_price, xrp_price, ltc_price

def sell_limit():
    btc_unit = binance.fetch_balance()["BTC"]['free']
    eth_unit = binance.fetch_balance()["ETH"]['free']
    xrp_unit = binance.fetch_balance()["XRP"]['free']
    ltc_unit = binance.fetch_balance()["LTC"]['free']
    try:
        if btc_unit > 0:
            btc_price = sellable()[0]
            binance.create_limit_sell_order("BTC/USDT", btc_unit, btc_price)
    except Exception as e:
        logging.info("btc sell error : " + str(e))

    try:
        if eth_unit > 0:
            eth_price = sellable()[1]
            binance.create_limit_sell_order("ETH/USDT", eth_unit, eth_price)
    except Exception as e:
        logging.info("eth sell error : " + str(e))

    try:
        if xrp_unit > 0:
            xrp_price = sellable()[2]
            binance.create_limit_sell_order("XRP/USDT", xrp_unit, xrp_price)
    except Exception as e:
        logging.info("xrp sell error : " + str(e))

    try:    
        if ltc_unit > 0:
            ltc_price = sellable()[3]
            binance.create_limit_sell_order("LTC/USDT", ltc_unit, ltc_price)
    except Exception as e:
        logging.info("ltc sell error : " + str(e))

def get_current_price(ticker):
    price = binance.fetch_ticker(ticker)
    price = price['close']
    return price


now = datetime.datetime.now()
nine = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=10, minutes=16)
if now > nine:
    nine = nine + datetime.timedelta(1)

a = 0
while a == 0:
    try:
        btc_open = get_open("BTC/USDT")
        btc_ma5 = get_ma5("BTC/USDT")
        btc_target = get_target_price("BTC/USDT")
        btc_status = 0

        eth_open = get_open("ETH/USDT")
        eth_ma5 = get_ma5("ETH/USDT")
        eth_target = get_target_price("ETH/USDT")
        eth_status = 0

        xrp_open = get_open("XRP/USDT")
        xrp_ma5 = get_ma5("XRP/USDT")
        xrp_target = get_target_price("XRP/USDT")
        xrp_status = 0

        ltc_open = get_open("LTC/USDT")
        ltc_ma5 = get_ma5("LTC/USDT")
        ltc_target = get_target_price("LTC/USDT")
        ltc_status = 0

        balance = binance.fetch_balance()['USDT']['free']
        logging.info("initial balance(USDT) : " + str(balance))
        a = 1
    except Exception as e:
        logging.info("initiating error : '" + str(e) + "' try again in 5 sec")
        time.sleep(5)

while True:
    try:
        now = datetime.datetime.now()
        if nine < now:
            sell_limit()
            time.sleep(60)
            nine = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=8, minutes=59)
            btc_target = get_target_price("BTC/USDT")
            eth_target = get_target_price("ETH/USDT")
            xrp_target = get_target_price("XRP/USDT")
            ltc_target = get_target_price("LTC/USDT")
            btc_ma5 = get_ma5("BTC/USDT")
            eth_ma5 = get_ma5("ETH/USDT")
            xrp_ma5 = get_ma5("XRP/USDT")
            ltc_ma5 = get_ma5("LTC/USDT")
            btc_open = get_open("BTC/USDT")
            eth_open = get_open("ETH/USDT")
            xrp_open = get_open("XRP/USDT")
            ltc_open = get_open("LTC/USDT")
            btc_status = 0
            eth_status = 0
            xrp_status = 0
            ltc_status = 0
            balance = binance.fetch_balance()['USDT']['free']
            logging.info("balance(USDT) : " + str(balance))

        btc_current_price = get_current_price("BTC/USDT")
        eth_current_price = get_current_price("ETH/USDT")
        xrp_current_price = get_current_price("XRP/USDT")
        ltc_current_price = get_current_price("LTC/USDT")

        if btc_current_price > btc_target and btc_status == 0 and btc_open > btc_ma5:
            buy_btc()
            logging.info("BTC get")
            btc_status = 1

        if eth_current_price > eth_target and eth_status == 0 and eth_open > eth_ma5:
            buy_eth()
            logging.info("ETH get")
            eth_status = 1

        if xrp_current_price > xrp_target and xrp_status == 0 and xrp_open > xrp_ma5:
            buy_xrp()
            logging.info("XRP get")
            xrp_status = 1

        if ltc_current_price > ltc_target and ltc_status == 0 and ltc_open > ltc_ma5:
            buy_ltc()
            logging.info("LTC get")
            ltc_status = 1
            
    except Exception as e:
        logging.info("programm error : " + str(e))
    time.sleep(1)