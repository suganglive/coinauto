import websockets
import asyncio
import json
import upbit as up
import time
import datetime
import logging
import upbase as pb
import uprank20 as rk
import math

logging.basicConfig(filename='son.log', level=logging.INFO, format='%(asctime)s:%(message)s')

access_key = "a"
secret_key = "b"
upbit = up.Up(access_key, secret_key)

# with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
#     lines = f.readlines()
#     access_key = lines[1].strip()
#     secret_key = lines[2].strip()
#     upbit = upbit.Up(access_key, secret_key)

target_v = 0.3
amount = 2
base = '16h'
base_time = 16
mas = [5, 10, 20]

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

def get_ma(ticker):
    dct = {}
    for ma in mas:
        df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = (ma+1)*24)
        open = df['open']
        movingavg = open.rolling(window=ma).mean()
        dct[ma] = movingavg[-1]
    return dct

def buyable(price):
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
    return price

def get_target_price(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = 72)
    today = df.iloc[-1]
    t_open = today['open']
    range = get_range(ticker)
    movingavg = get_ma(ticker)
    count = 0
    for ma in mas:
        if t_open > movingavg[ma]:
            count += 1
    if count > 2:
        k = 0.3
    elif count > 1:
        k = 0.5
    else:
        k = 0.8

    target_price = t_open + range * k
    if target_price < 5000:
        target_price = buyable(target_price)
    return target_price

def buy_market(ticker, krw, percentage):
    krw = krw * percentage
    upbit.buy_market_order(ticker, krw)

def sell_market(ticker, volume):
    upbit.sell_market_order(ticker, volume)

async def program():
    uri = "wss://api.upbit.com/websocket/v1"
    base = '16h'
    base_time = 16
    dic = {}

    now = datetime.datetime.now()
    end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=base_time)
    if now > end:
        end = end + datetime.timedelta(1)
    tickers = rk.get_ranks(base = base)
    coin1 = tickers[0]
    coin2 = tickers[1]
    coins = [coin1, coin2]

    a = 0
    while a == 0:
        try:
            for i in range(1, -1, -1):
                dic[f'coin{i}_open'] = get_open(coins[i])
                movingavg = get_ma(coins[i])
                dic[f'coin{i}_ma5'] = movingavg[5]
                dic[f'coin{i}_ma10'] = movingavg[10]
                dic[f'coin{i}_ma20'] = movingavg[20]
                if dic[f'coin{i}_open'] < dic[f'coin{i}_ma10'] and dic[f'coin{i}_open'] < dic[f'coin{i}_ma5'] and dic[f'coin{i}_open'] < dic[f'coin{i}_ma20']:
                    logging.info(f"coin excluded : {coins[i]}, open : {dic[f'coin{i}_open']}, ma10 : {dic[f'coin{i}_ma10']}")
                    coins.pop(i) 

            for i in range(0,len(coins)):
                dic[f'coin{i}_open'] = get_open(coins[i])
                movingavg = get_ma(coins[i])
                dic[f'coin{i}_ma5'] = movingavg[5]
                dic[f'coin{i}_ma10'] = movingavg[10]
                dic[f'coin{i}_ma20'] = movingavg[20]
                dic[f'coin{i}_target'] = get_target_price(coins[i])
                dic[f'coin{i}_percent'] = get_percentage(coins[i])
                dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                dic[f'coin{i}_current_price'] = 0
                if dic[f'coin{i}_volume'] != 0:
                    dic[f'coin{i}_status'] = 1
                else:
                    dic[f'coin{i}_status'] = 0
                logging.info(f"coin{i} = {coins[i]}, coin{i}_target = {dic[f'coin{i}_target']}, coin{i}_percent = {dic[f'coin{i}_percent']}, coin{i}_status = {dic[f'coin{i}_status']}")

            krw = round(upbit.get_balance("KRW"))
            logging.info(f"krw_balance : {krw}")
            a = 1
        except Exception as e:
            logging.info("default value error : " + str(e))
            time.sleep(10)

    logging.info("program started")

    while True:
        async with websockets.connect(uri, ping_interval=60) as websocket:
            subscribe_fmt = [{"ticket":"test"}, {"type":"ticker", "codes":coins, "isOnlyRealtime": True}, {"format":"SIMPLE"}]
            subscribe_data = json.dumps(subscribe_fmt)
            await websocket.send(subscribe_data)

            if len(coins) == 0 and end > now:
                now = datetime.datetime.now()
                logging.info("There's no coin to invest. rest for 1 day")
                time.sleep(3600)
                continue

            while True:
                try:
                    now = datetime.datetime.now()
                    if end < now:
                        for i in range(0, len(coins)):
                            if dic[f'coin{i}_volume'] != 0:
                                sell_market(coins[i], dic[f'coin{i}_volume'])

                        tickers = rk.get_ranks(base = base)
                        coin1 = tickers[0]
                        coin2 = tickers[1]
                        coins = [coin1, coin2]

                        for i in range(1, -1, -1):
                            dic[f'coin{i}_open'] = get_open(coins[i])
                            movingavg = get_ma(coins[i])
                            dic[f'coin{i}_ma5'] = movingavg[5]
                            dic[f'coin{i}_ma10'] = movingavg[10]
                            dic[f'coin{i}_ma20'] = movingavg[20]
                            if dic[f'coin{i}_open'] < dic[f'coin{i}_ma10'] and dic[f'coin{i}_open'] < dic[f'coin{i}_ma5'] and dic[f'coin{i}_open'] < dic[f'coin{i}_ma20']:
                                logging.info(f"coin excluded : {coins[i]}, open : {dic[f'coin{i}_open']}, ma10 : {dic[f'coin{i}_ma10']}")
                                coins.pop(i) 

                        for i in range(0,len(coins)):
                            dic[f'coin{i}_open'] = get_open(coins[i])
                            movingavg = get_ma(coins[i])
                            dic[f'coin{i}_ma5'] = movingavg[5]
                            dic[f'coin{i}_ma10'] = movingavg[10]
                            dic[f'coin{i}_ma20'] = movingavg[20]
                            dic[f'coin{i}_target'] = get_target_price(coins[i])
                            dic[f'coin{i}_percent'] = get_percentage(coins[i])
                            dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                            dic[f'coin{i}_current_price'] = 0
                            if dic[f'coin{i}_volume'] != 0:
                                dic[f'coin{i}_status'] = 1
                            else:
                                dic[f'coin{i}_status'] = 0
                            logging.info(f"coin{i} = {coins[i]}, coin{i}_target = {dic[f'coin{i}_target']}, coin{i}_percent = {dic[f'coin{i}_percent']}, coin{i}_status = {dic[f'coin{i}_status']}")

                        krw1 = round(upbit.get_balance("KRW"))
                        profit = krw1/krw -1
                        logging.info(f"profit : {profit}")
                        krw = krw1
                        end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=base_time)
                        logging.info(f"krw_balance : {krw}")
                        break

                    data = await websocket.recv()
                    data = json.loads(data)
                    if data['cd'] == coins[0]:
                        dic['coin0_current_price'] = data['tp']
                    elif data['cd'] == coins[1]:
                        dic['coin1_current_price'] = data['tp']

                    for i in range(0, len(coins)):
                        if dic[f'coin{i}_current_price'] >= dic[f'coin{i}_target'] and dic[f'coin{i}_status'] == 0 and (dic[f'coin{i}_open'] >= dic[f'coin{i}_ma10'] or dic[f'coin{i}_open'] >= dic[f'coin{i}_ma5'] or dic[f'coin{i}_open'] >= dic[f'coin{i}_ma10']):
                            try:
                                buy_market(coins[i], krw, dic[f'coin{i}_percent'])
                                time.sleep(1)
                                dic[f'coin{i}_status'] = 1
                                dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                                avg_price = (krw * dic[f'coin{i}_percent'])/dic[f'coin{i}_volume']
                                logging.info(f"coin{i} get, current price = {dic[f'coin{i}_current_price']}, target = {dic[f'coin{i}_target']}")
                                logging.info(f"coin{i}_volume = {dic[f'coin{i}_volume']}, avg price = {avg_price}, slippage = {(avg_price/dic[f'coin{i}_target'])-1}")
                            except Exception as e:
                                logging.info(f"coin{i} buy error", str(e))

                except Exception as e:
                    logging.info("programm error : " + str(e))
                    break

async def main():
    await program()
asyncio.run(main())