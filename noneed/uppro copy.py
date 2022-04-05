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

# access_key = "a"
# secret_key = "b"
# upbit = pyupbit.Upbit(access_key, secret_key)

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[1].strip()
    secret_key = lines[2].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

k = 0.5
target_v = 0.2
m = 10
amount = 2
base = '11h'
base_time = 11

tickers = rk.get_tickers(base = base)
coin1 = tickers[0]
coin2 = tickers[1]

def get_range(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base)
    y_day = df.iloc[-2]

    y_high = y_day['high']
    y_low = y_day['low']
    range = y_high - y_low
    return range

def get_open(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base)
    today = df.iloc[-1]
    open = today['open']
    return open

def get_y_open(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base)
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
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base)
    today = df.iloc[-1]

    t_open = today['open']
    range = get_range(ticker)
    target_price = t_open + range * k
    return target_price

def get_ma10(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = (m+1)*24)
    open = df['open']
    ma = open.rolling(window=m).mean()
    return ma[-1]

def buyable(ticker):
    price = get_target_price(ticker)
    price = price * 1.002
    if price - 1 < 0:
        if price * 10 - 1 < 0:
            price = price * 10000
            price = math.floor(price)
            price = price + 1
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
    elif len(str(math.floor(price))) == 4:
        if price % 10 <= 5: 
            price = price / 10
            price = math.floor(price)
            price = price * 10
            price = price + 5
        else:
            price = price / 10
            price = math.floor(price)
            price = price * 10
            price = price + 10
    elif len(str(math.floor(price))) == 5:
        price = price / 10
        price = math.floor(price)
        price = price + 1
        price = price * 10
    elif len(str(math.floor(price))) == 6:
        if (price/10) % 10 <= 5: 
            price = price / 100
            price = math.floor(price)
            price = price * 100
            price = price + 50
        else:
            price = price / 100
            price = math.floor(price)
            price = price * 100
            price = price + 100
    elif len(str(math.floor(price))) >=7:
            price = price / 1000
            price = math.floor(price)
            price = price * 1000
            price = price + 1000
    return price

def buy_limit(ticker, krw):
    percentage = get_percentage(ticker)
    krw = krw * percentage
    price = buyable(ticker)
    # target = get_target_price(ticker)
    # unit = krw/float(price)
    upbit.buy_limit_order(ticker, price, 100)

def sell_price(ticker):
    price = pyupbit.get_current_price(ticker)
    return price

def sellable(ticker):
    price = sell_price(ticker)
    price = price * 0.998
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

def sell_limit(ticker):
    try:
        unit = upbit.get_balance(ticker[4:])
        price = sellable(ticker)
        upbit.sell_limit_order(ticker, price, unit)
    except Exception as e:
        logging.info(str(ticker) + "/sell error/" + str(e))

now = datetime.datetime.now()
end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=base_time)

if now > end:
    end = end + datetime.timedelta(1)

a = 0
while a == 0:
    try:
        coin1_open = get_open(coin1)
        coin1_ma10 = get_ma10(coin1)
        coin1_target = get_target_price(coin1)
        coin1_percent = get_percentage(coin1)
        coin1_status = 0
        if upbit.get_balance(coin1) != 0:
            coin1_status = 1

        coin2_open = get_open(coin2)
        coin2_ma10 = get_ma10(coin2)
        coin2_target = get_target_price(coin2)
        coin2_percent = get_percentage(coin2)
        coin2_status = 0
        if upbit.get_balance(coin2) != 0:
            coin2_status = 1

        krw = upbit.get_balance("KRW")
        krw = round(krw)
        logging.info(f"coin1 = {coin1}, coin1_percent = {coin1_percent}, coin1_open : {coin1_open}, coin1_ma10 : {coin1_ma10}, coin1_target : {coin1_target}, coin1_status : {coin1_status}")
        logging.info(f"coin2 = {coin2}, coin2_percent = {coin2_percent}, coin2_open : {coin2_open}, coin2_ma10 : {coin2_ma10}, coin2_target : {coin2_target}, coin2_status : {coin2_status}")
        logging.info(f"krw_balance : {krw}")
        a = 1
    except Exception as e:
        logging.info("default value error : " + str(e))
        time.sleep(1)

logging.info("program started")

async def program():
    global coin1
    global coin2
    global now
    global end
    global coin1_open
    global coin1_ma10
    global coin1_target
    global coin1_percent
    global coin1_status
    global coin2_open
    global coin2_ma10
    global coin2_target
    global coin2_percent
    global coin2_status
    global k
    global target_v
    global m
    global amount
    global base
    global base_time
    global krw

    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [{"ticket":"test"}, {"type":"ticker", "codes":[coin1, coin2], "isOnlyRealtime": True}, {"format":"SIMPLE"}]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        if now > end:
            end = end + datetime.timedelta(1)
        while True:
            try:
                now = datetime.datetime.now()
                if end < now:
                    for ticker in tickers:
                        if upbit.get_order(ticker):
                            logging.info(ticker, "buy order failed, cancle")
                            upbit.cancel_order(upbit.get_order(ticker)[0]['uuid'])
                    for ticker in tickers:
                        if upbit.get_balance(ticker) != 0:
                            sell_limit(ticker)
                            logging.info(ticker, "sell order submitted")

                    tickers = rk.get_tickers(base = base)
                    coin1 = tickers[0]
                    coin2 = tickers[1]
                    
                    coin1_percent = get_percentage(coin1)
                    coin2_percent = get_percentage(coin2)
                    
                    coin1_target = get_target_price(coin1)
                    coin2_target = get_target_price(coin2)
                    
                    coin1_ma10 = get_ma10(coin1)
                    coin2_ma10 = get_ma10(coin2)
                    
                    coin1_open = get_open(coin1)
                    coin2_open = get_open(coin2)
                    
                    coin1_status = 0
                    coin2_status = 0
                    
                    krw1 = upbit.get_balance("KRW")
                    profit = krw1/krw -1
                    logging.info(f"profit : {profit}")
                    krw = upbit.get_balance("KRW")
                    krw = round(krw)
                    end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=base_time)
                    logging.info(f"coin1 = {coin1}, coin1_percent = {coin1_percent}, coin1_open : {coin1_open}, coin1_ma10 : {coin1_ma10}, coin1_target : {coin1_target}, coin1_status : {coin1_status}")
                    logging.info(f"coin2 = {coin2}, coin2_percent = {coin2_percent}, coin2_open : {coin2_open}, coin2_ma10 : {coin2_ma10}, coin2_target : {coin2_target}, coin2_status : {coin2_status}")
                    logging.info(f"krw_balance : {krw}")

                data = await websocket.recv()
                data = json.loads(data)
                if data['cd'] == coin1:
                    coin1_current_price = data['tp']
                elif data['cd'] == coin2:
                    coin2_current_price = data['tp']
                
                if coin1_current_price > 1 and coin1_status == 0 and coin1_open >= coin1_ma10:
                    try:
                        # buy_limit(coin1, krw)
                        print("buy coin1")
                        coin1_status = 1
                        logging.info("coin1 get")
                    except Exception as e:
                        logging.info("coin1 buy error", str(e))

                if coin2_current_price > coin2_target and coin2_status == 0 and coin2_open >= coin2_ma10:
                    try:
                        # buy_limit(coin2, krw)
                        print("buy coin2")
                        coin2_status = 1
                        logging.info("coin2 get")
                    except Exception as e:
                        logging.info("coin2 buy error", str(e))
                print(now)
            except Exception as e:
                logging.info("programm error : " + str(e))

async def main():
    await program()

asyncio.run(main())
