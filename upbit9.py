# upbit8 + 거래량 기준 코인 선정
import pyupbit
import time
import datetime
import math
import logging
import pyupbase as pb
import volume1 as v1

logging.basicConfig(filename='upbit8.log', level=logging.INFO, format='%(asctime)s:%(message)s')

# access_key = "a"
# secret_key = "b"
# upbit = pyupbit.Upbit(access_key, secret_key)

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

tickers = v1.get_tickers()
coin1 = tickers[0]
coin2 = tickers[1]
coin3 = tickers[2]
coin4 = tickers[3]
coin5 = tickers[4]
k = 0.5
target_v = 0.05

def get_range(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker)
    y_day = df.iloc[-2]

    y_high = y_day['high']
    y_low = y_day['low']
    range = y_high - y_low
    return range

def get_open(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker)
    today = df.iloc[-1]
    open = today['open']
    return open

def get_y_open(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker)
    today = df.iloc[-2]
    open = today['open']
    return open

def get_percentage(ticker):
    range = get_range(ticker)
    y_open = get_y_open(ticker)
    range_ratio = range/y_open
    if target_v > range_ratio:
        percentage = 1/5
    else:
        percentage = (1/5)*(target_v/range_ratio)
    return percentage

def get_target_price(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker)
    today = df.iloc[-1]

    t_open = today['open']
    range = get_range(ticker)
    target_price = t_open + range * k
    target_price = target_price * 1.002
    return target_price

def get_ma5(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker)
    open = df['open']
    ma = open.rolling(window=5).mean()
    return ma[-1]

def buyable(ticker):
    target = pyupbit.get_tick_size(get_target_price(ticker))
    return target

def buy_limit(ticker, krw):
    percentage = get_percentage(ticker)
    krw = krw * percentage
    price = buyable(ticker)
    unit = krw/float(price)
    upbit.buy_limit_order(ticker, price, unit)

def sell_price(ticker):
    price = pyupbit.get_current_price(ticker)
    price = price * 0.998
    return price

def sellable(ticker):
    price = pyupbit.get_tick_size(sell_price(ticker))
    return price

def sell_limit(ticker):
    try:
        unit = upbit.get_balance(ticker[4:])
        price = sellable(ticker)
        upbit.sell_limit_order(ticker, price, unit)
    except Exception as e:
        logging.info(str(ticker) + "/sell error/" + str(e))

def sell_market(ticker):
    try:
        unit = upbit.get_balance(ticker[4:])
        upbit.sell_market_order(ticker, unit)
    except Exception as e:
        logging.info(str(ticker) + "/market sell error/" + str(e))

now = datetime.datetime.now()
ten = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=10)

if now > ten:
    ten = ten + datetime.timedelta(1)

a = 0
while a == 0:
    try:
        coin1_open = get_open(coin1)
        coin1_ma5 = get_ma5(coin1)
        coin1_target = get_target_price(coin1)
        coin1_percent = get_percentage(coin1)
        coin1_status = 0

        coin2_open = get_open(coin2)
        coin2_ma5 = get_ma5(coin2)
        coin2_target = get_target_price(coin2)
        coin2_percent = get_percentage(coin2)
        coin2_status = 0

        coin3_open = get_open(coin3)
        coin3_ma5 = get_ma5(coin3)
        coin3_target = get_target_price(coin3)
        coin3_percent = get_percentage(coin3)
        coin3_status = 0

        coin4_open = get_open(coin4)
        coin4_ma5 = get_ma5(coin4)
        coin4_target = get_target_price(coin4)
        coin4_percent = get_percentage(coin4)
        coin4_status = 0

        coin5_open = get_open(coin5)
        coin5_ma5 = get_ma5(coin5)
        coin5_target = get_target_price(coin5)
        coin5_percent = get_percentage(coin5)
        coin5_status = 0

        krw = upbit.get_balance("KRW")
        krw = round(krw)
        logging.info(f"coin1 = {coin1}, coin1_percent = {coin1_percent}, coin1_open : {coin1_open}, coin1_ma5 : {coin1_ma5}, coin1_target : {coin1_target}, coin1_status : {coin1_status}")
        logging.info(f"coin2 = {coin2}, coin2_percent = {coin2_percent}, coin2_open : {coin2_open}, coin2_ma5 : {coin2_ma5}, coin2_target : {coin2_target}, coin2_status : {coin2_status}")
        logging.info(f"coin3 = {coin3}, coin3_percent = {coin3_percent}, coin3_open : {coin3_open}, coin3_ma5 : {coin3_ma5}, coin3_target : {coin3_target}, coin3_status : {coin3_status}")
        logging.info(f"coin4 = {coin4}, coin4_percent = {coin4_percent}, coin4_open : {coin4_open}, coin4_ma5 : {coin4_ma5}, coin4_target : {coin4_target}, coin4_status : {coin4_status}")
        logging.info(f"coin5 = {coin5}, coin5_percent = {coin5_percent}, coin5_open : {coin5_open}, coin5_ma5 : {coin5_ma5}, coin5_target : {coin5_target}, coin5_status : {coin5_status}")
        logging.info(f"krw_balance : {krw}")
        a = 1
    except Exception as e:
        logging.info("default value error : " + str(e))
        time.sleep(1)

logging.info("program started")

while True:
    try:
        now = datetime.datetime.now()
        if ten < now:
            for ticker in tickers:
                if upbit.get_balance(ticker) != 0:
                    sell_limit(ticker)
                    logging.info(ticker, "sell order submitted")
            tickers = v1.get_tickers()
            coin1 = tickers[0]
            coin2 = tickers[1]
            coin3 = tickers[2]
            coin4 = tickers[3]
            coin5 = tickers[4]

            coin1_percent = get_percentage(coin1)
            coin2_percent = get_percentage(coin2)
            coin3_percent = get_percentage(coin3)
            coin4_percent = get_percentage(coin4)
            coin5_percent = get_percentage(coin5)
            
            coin1_target = get_target_price(coin1)
            coin2_target = get_target_price(coin2)
            coin3_target = get_target_price(coin3)
            coin4_target = get_target_price(coin4)
            coin5_target = get_target_price(coin5)
            
            coin1_ma5 = get_ma5(coin1)
            coin2_ma5 = get_ma5(coin2)
            coin3_ma5 = get_ma5(coin3)
            coin4_ma5 = get_ma5(coin4)
            coin5_ma5 = get_ma5(coin5)

            coin1_open = get_open(coin1)
            coin2_open = get_open(coin2)
            coin3_open = get_open(coin3)
            coin4_open = get_open(coin4)
            coin5_open = get_open(coin5)
            
            coin1_status = 0
            coin2_status = 0
            coin3_status = 0
            coin4_status = 0
            coin5_status = 0

            krw1 = upbit.get_balance("KRW")
            profit = krw1/krw -1
            logging.info(f"profit : {profit}")
            krw = upbit.get_balance("KRW")
            krw = round(krw)
            ten = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=10)
            logging.info(f"coin1 = {coin1}, coin1_percent = {coin1_percent}, coin1_open : {coin1_open}, coin1_ma5 : {coin1_ma5}, coin1_target : {coin1_target}, coin1_status : {coin1_status}")
            logging.info(f"coin2 = {coin2}, coin2_percent = {coin2_percent}, coin2_open : {coin2_open}, coin2_ma5 : {coin2_ma5}, coin2_target : {coin2_target}, coin2_status : {coin2_status}")
            logging.info(f"coin3 = {coin3}, coin3_percent = {coin3_percent}, coin3_open : {coin3_open}, coin3_ma5 : {coin3_ma5}, coin3_target : {coin3_target}, coin3_status : {coin3_status}")
            logging.info(f"coin4 = {coin4}, coin4_percent = {coin4_percent}, coin4_open : {coin4_open}, coin4_ma5 : {coin4_ma5}, coin4_target : {coin4_target}, coin4_status : {coin4_status}")
            logging.info(f"coin5 = {coin5}, coin5_percent = {coin5_percent}, coin5_open : {coin5_open}, coin5_ma5 : {coin5_ma5}, coin5_target : {coin5_target}, coin5_status : {coin5_status}")
            logging.info(f"krw_balance : {krw}")

        coin1_current_price = pyupbit.get_current_price(coin1)
        coin2_current_price = pyupbit.get_current_price(coin2)
        coin3_current_price = pyupbit.get_current_price(coin3)
        coin4_current_price = pyupbit.get_current_price(coin4)
        coin5_current_price = pyupbit.get_current_price(coin5)
        
        if coin1_current_price > coin1_target and coin1_status == 0 and coin1_open > coin1_ma5:
            try:
                buy_limit(coin1, krw)
                coin1_status = 1
                logging.info("coin1 get")
            except Exception as e:
                logging.info("coin1 buy error", str(e))

        if coin2_current_price > coin2_target and coin2_status == 0 and coin2_open > coin2_ma5:
            try:
                buy_limit(coin2, krw)
                coin2_status = 1
                logging.info("coin2 get")
            except Exception as e:
                logging.info("coin2 buy error", str(e))

        if coin3_current_price > coin3_target and coin3_status == 0 and coin3_open > coin3_ma5:
            try:
                buy_limit(coin3, krw)
                coin3_status = 1
                logging.info("coin3 get")
            except Exception as e:
                logging.info("coin3 buy error", str(e))

        if coin4_current_price > coin4_target and coin4_status == 0 and coin4_open > coin4_ma5:
            try:
                buy_limit(coin4, krw)
                
                coin4_status = 1
                logging.info("coin4 get")
            except Exception as e:
                logging.info("coin4 buy error", str(e))

        if coin5_current_price > coin5_target and coin5_status == 0 and coin5_open > coin5_ma5:
            try:
                buy_limit(coin5, krw)
                
                coin5_status = 1
                logging.info("coin5 get")
            except Exception as e:
                logging.info("coin5 buy error", str(e))
        
    except Exception as e:
        logging.info("programm error : " + str(e))
    time.sleep(1)