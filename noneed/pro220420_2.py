# 나중에 랭킹도 가볍게 돌리기 가능?
# 자료수집 빠르게 -> 처음엔 걍 Ma10, open만 검색
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

logging.basicConfig(filename='pro220420_2.log', level=logging.INFO, format='%(asctime)s:%(message)s')

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
amount = 20
base = '11h'
base_time = 11

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

def get_target_price(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = 72)
    today = df.iloc[-1]

    t_open = today['open']
    range = get_range(ticker)
    target_price = t_open + range * k
    if target_price < 5000:
        target_price = buyable(target_price)
    return target_price

def get_ma10(ticker):
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, base = base, count = (m+1)*24)
    open = df['open']
    ma = open.rolling(window=m).mean()
    return ma[-1]

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

def buy_market(ticker, krw, percentage):
    krw = krw * percentage
    upbit.buy_market_order(ticker, krw)

def sell_market(ticker, volume):
    upbit.sell_market_order(ticker, volume)

async def program():
    uri = "wss://api.upbit.com/websocket/v1"
    base = '11h'
    base_time = 11
    dic = {}

    now = datetime.datetime.now()
    end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=base_time)
    if now > end:
        end = end + datetime.timedelta(1)
    tickers = rk.get_tickers(base = base)
    coin1 = tickers[0]
    coin2 = tickers[1]
    coin3 = tickers[2]
    coin4 = tickers[3]
    coin5 = tickers[4]
    coin6 = tickers[5]
    coin7 = tickers[6]
    coin8 = tickers[7]
    coin9 = tickers[8]
    coin10 = tickers[9]
    coin11 = tickers[10]
    coin12 = tickers[11]
    coin13 = tickers[12]
    coin14 = tickers[13]
    coin15 = tickers[14]
    coin16 = tickers[15]
    coin17 = tickers[16]
    coin18 = tickers[17]
    coin19 = tickers[18]
    coin20 = tickers[19]
    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20]

    a = 0
    while a == 0:
        try:
            for i in range(19, -1, -1):
                dic[f'coin{i}_open'] = get_open(coins[i])
                dic[f'coin{i}_ma10'] = get_ma10(coins[i])
                if dic[f'coin{i}_open'] < dic[f'coin{i}_ma10']:
                    logging.info(f"coin excluded : {coins[i]}, open : {dic[f'coin{i}_open']}, ma10 : {dic[f'coin{i}_ma10']}")
                    coins.pop(i) 

            for i in range(0,len(coins)):
                dic[f'coin{i}_open'] = get_open(coins[i])
                dic[f'coin{i}_ma10'] = get_ma10(coins[i])
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
            krw = 10000000
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

            while True:
                try:
                    now = datetime.datetime.now()
                    if end < now:
                        for i in range(0, len(coins)):
                            if dic[f'coin{i}_volume'] != 0:
                                sell_market(coins[i], dic[f'coin{i}_volume'])

                        tickers = rk.get_tickers(base = base)
                        coin1 = tickers[0]
                        coin2 = tickers[1]
                        coin3 = tickers[2]
                        coin4 = tickers[3]
                        coin5 = tickers[4]
                        coin6 = tickers[5]
                        coin7 = tickers[6]
                        coin8 = tickers[7]
                        coin9 = tickers[8]
                        coin10 = tickers[9]
                        coin11 = tickers[10]
                        coin12 = tickers[11]
                        coin13 = tickers[12]
                        coin14 = tickers[13]
                        coin15 = tickers[14]
                        coin16 = tickers[15]
                        coin17 = tickers[16]
                        coin18 = tickers[17]
                        coin19 = tickers[18]
                        coin20 = tickers[19]
                        coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20]

                        for i in range(19, -1, -1):
                            dic[f'coin{i}_open'] = get_open(coins[i])
                            dic[f'coin{i}_ma10'] = get_ma10(coins[i])
                            if dic[f'coin{i}_open'] < dic[f'coin{i}_ma10']:
                                logging.info(f"coin excluded : {coins[i]}, open : {dic[f'coin{i}_open']}, ma10 : {dic[f'coin{i}_ma10']}")
                                coins.pop(i)
                        
                        for i in range(0, len(coins)):
                            dic[f'coin{i}_open'] = get_open(coins[i])
                            dic[f'coin{i}_ma10'] = get_ma10(coins[i])
                            dic[f'coin{i}_target'] = get_target_price(coins[i])
                            dic[f'coin{i}_percent'] = get_percentage(coins[i])
                            dic[f'coin{i}_status'] = 0
                            dic[f'coin{i}_current_price'] = 0
                            dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                            if dic[f'coin{i}_volume'] != 0:
                                dic[f'coin{i}_status'] = 1
                            else:
                                dic[f'coin{i}_status'] = 0                            
                            logging.info(f"coin{i} = {coins[i]}, coin{i}_target = {dic[f'coin{i}_target']}, coin{i}_percent = {dic[f'coin{i}_percent']}, coin{i}_status = {dic[f'coin{i}_status']}")

                        # krw1 = round(upbit.get_balance("KRW"))
                        # profit = krw1/krw -1
                        # logging.info(f"profit : {profit}")
                        # krw = krw1
                        krw = 10000000
                        end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=base_time)
                        logging.info(f"krw_balance : {krw}")
                        break

                    data = await websocket.recv()
                    data = json.loads(data)
                    if data['cd'] == coins[0]:
                        dic['coin0_current_price'] = data['tp']
                    elif data['cd'] == coins[1]:
                        dic['coin1_current_price'] = data['tp']
                    elif data['cd'] == coins[2]:
                        dic['coin2_current_price'] = data['tp']
                    elif data['cd'] == coins[3]:
                        dic['coin3_current_price'] = data['tp']
                    elif data['cd'] == coins[4]:
                        dic['coin4_current_price'] = data['tp']
                    elif data['cd'] == coins[5]:
                        dic['coin5_current_price'] = data['tp']
                    elif data['cd'] == coins[6]:
                        dic['coin6_current_price'] = data['tp']
                    elif data['cd'] == coins[7]:
                        dic['coin7_current_price'] = data['tp']
                    elif data['cd'] == coins[8]:
                        dic['coin8_current_price'] = data['tp']
                    elif data['cd'] == coins[9]:
                        dic['coin9_current_price'] = data['tp']
                    elif data['cd'] == coins[10]:
                        dic['coin10_current_price'] = data['tp']
                    elif data['cd'] == coins[11]:
                        dic['coin11_current_price'] = data['tp']
                    elif data['cd'] == coins[12]:
                        dic['coin12_current_price'] = data['tp']
                    elif data['cd'] == coins[13]:
                        dic['coin13_current_price'] = data['tp']
                    elif data['cd'] == coins[14]:
                        dic['coin14_current_price'] = data['tp']
                    elif data['cd'] == coins[15]:
                        dic['coin15_current_price'] = data['tp']
                    elif data['cd'] == coins[16]:
                        dic['coin16_current_price'] = data['tp']
                    elif data['cd'] == coins[17]:
                        dic['coin17_current_price'] = data['tp']
                    elif data['cd'] == coins[18]:
                        dic['coin18_current_price'] = data['tp']
                    elif data['cd'] == coins[19]:
                        dic['coin19_current_price'] = data['tp']

                    for i in range(0, len(coins)):
                        if dic[f'coin{i}_current_price'] >= dic[f'coin{i}_target'] and dic[f'coin{i}_status'] == 0 and dic[f'coin{i}_open'] >= dic[f'coin{i}_ma10']:
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