# 2022 04 06 시작 From noneed/uppro3.py h>t -> h>=t 변경. 이유 : 백원대 코인들 하나 올라가면 1퍼씩 올라감.
# 시장가 거래로 변경
# 매수, 매도 주문 속도 향상 // 딕셔너리 사용 // 함수 사용에서 변수 바로 사용으로 변경 // 중간에 내가 임의로 사면 11시에 안팔림.
#수정필요(에러안나게 or 에러 나도 복구) programming code error -> break 
#programming code error 2 -> 일단 서버 구분으로 통제해보자
# 500원 이하 코인들 -> 타겟 buyable로 통일, 슬리피지 잡기 위해서
# 나중에 랭킹도 가볍게 돌리기 가능?

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

logging.basicConfig(filename='pro220418.log', level=logging.INFO, format='%(asctime)s:%(message)s')

access_key = "a"
secret_key = "b"
upbit = pyupbit.Upbit(access_key, secret_key)

# with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
#     lines = f.readlines()
#     access_key = lines[1].strip()
#     secret_key = lines[2].strip()
#     upbit = pyupbit.Upbit(access_key, secret_key)

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
    if target_price <= 500:
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
            for i in range(0,20):
                dic[f'coin{i}_open'] = get_open(coins[i])
                dic[f'coin{i}_ma10'] = get_ma10(coins[i])
                dic[f'coin{i}_target'] = get_target_price(coins[i])
                dic[f'coin{i}_percent'] = get_percentage(coins[i])
                dic[f'coin{i}_status'] = 0
                dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                dic[f'coin{i}_current_price'] = 0
                if dic[f'coin{i}_volume'] != 0:
                    dic[f'coin{i}_status'] = 1
                else:
                    dic[f'coin{i}_volume'] = 0
                logging.info(f"coin{i} = {coins[i]}, coin{i}_open = {dic[f'coin{i}_open']}, coin{i}_target = {dic[f'coin{i}_target']}, coin{i}_ma10 = {dic[f'coin{i}_ma10']}, coin{i}_percent = {dic[f'coin{i}_percent']}, coin{i}_volume = {dic[f'coin{i}_volume']}")

            krw = round(upbit.get_balance("KRW"))
            logging.info(f"krw_balance : {krw}")
            a = 1
        except Exception as e:
            logging.info("default value error : " + str(e))
            time.sleep(10)

    logging.info("program started")
    
    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [{"ticket":"test"}, {"type":"ticker", "codes":coins, "isOnlyRealtime": True}, {"format":"SIMPLE"}]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            try:
                now = datetime.datetime.now()
                if end < now:
                    for i in coins:
                        if dic[f'coin{i}_volume'] != 0:
                            sell_market(coins[i], dic[f'coin{i}_volume'])
                            dic[f'coin{i}_volume'] = 0
                            dic[f'coin{i}_status'] = 0
                            logging.info(f"{coins[i]} sold")

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

                    for i in range(0,20):
                        dic[f'coin{i}_open'] = get_open(coins[i])
                        dic[f'coin{i}_ma10'] = get_ma10(coins[i])
                        dic[f'coin{i}_target'] = get_target_price(coins[i])
                        dic[f'coin{i}_percent'] = get_percentage(coins[i])
                        dic[f'coin{i}_status'] = 0
                        dic[f'coin{i}_current_price'] = 0
                        dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                        if dic[f'coin{i}_volume'] != 0:
                            dic[f'coin{i}_status'] = 1
                        logging.info(f"coin{i} = {coins[i]}, coin{i}_open = {dic[f'coin{i}_open']}, coin{i}_target = {dic[f'coin{i}_target']}, coin{i}_ma10 = {dic[f'coin{i}_ma10']}, coin{i}_percent = {dic[f'coin{i}_percent']}, coin{i}_volume = {dic[f'coin{i}_volume']}")

                    krw1 = round(upbit.get_balance("KRW"))
                    profit = krw1/krw -1
                    logging.info(f"profit : {profit}")
                    krw = krw1
                    end = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=base_time)
                    logging.info(f"krw_balance : {krw}")

                data = await websocket.recv()
                data = json.loads(data)
                if data['cd'] == coin1:
                    dic['coin0_current_price'] = data['tp']
                elif data['cd'] == coin2:
                    dic['coin1_current_price'] = data['tp']
                elif data['cd'] == coin3:
                    dic['coin2_current_price'] = data['tp']
                elif data['cd'] == coin4:
                    dic['coin3_current_price'] = data['tp']
                elif data['cd'] == coin5:
                    dic['coin4_current_price'] = data['tp']
                elif data['cd'] == coin6:
                    dic['coin5_current_price'] = data['tp']
                elif data['cd'] == coin7:
                    dic['coin6_current_price'] = data['tp']
                elif data['cd'] == coin8:
                    dic['coin7_current_price'] = data['tp']
                elif data['cd'] == coin9:
                    dic['coin8_current_price'] = data['tp']
                elif data['cd'] == coin10:
                    dic['coin9_current_price'] = data['tp']
                elif data['cd'] == coin11:
                    dic['coin10_current_price'] = data['tp']
                elif data['cd'] == coin12:
                    dic['coin11_current_price'] = data['tp']
                elif data['cd'] == coin13:
                    dic['coin12_current_price'] = data['tp']
                elif data['cd'] == coin14:
                    dic['coin13_current_price'] = data['tp']
                elif data['cd'] == coin15:
                    dic['coin14_current_price'] = data['tp']
                elif data['cd'] == coin16:
                    dic['coin15_current_price'] = data['tp']
                elif data['cd'] == coin17:
                    dic['coin16_current_price'] = data['tp']
                elif data['cd'] == coin18:
                    dic['coin17_current_price'] = data['tp']
                elif data['cd'] == coin19:
                    dic['coin18_current_price'] = data['tp']
                elif data['cd'] == coin20:
                    dic['coin19_current_price'] = data['tp']

                for i in range(0, 20):
                    if dic[f'coin{i}_current_price'] >= dic[f'coin{i}_target'] and dic[f'coin{i}_status'] == 0 and dic[f'coin{i}_current_open'] >= dic[f'coin{i}_ma10']:
                        try:
                            buy_market(coins[i], krw, dic[f'coin{i}_percent'])
                            time.sleep(1)
                            dic[f'coin{i}_status'] = 1
                            dic[f'coin{i}_volume'] = upbit.get_balance(coins[i])
                            logging.info(f"coin{i} get, current price = {dic[f'coin{i}_current_price']}, target = {dic[f'coin{i}_target']}")
                            logging.info(f"coin{i}_volume = {dic[f'coin{i}_volume']}, avg price = {(krw * dic[f'coin{i}_percent'])/dic[f'coin{i}_volume']}")
                        except Exception as e:
                            logging.info(f"coin{i} buy error", str(e))

            except Exception as e:
                logging.info("programm error : " + str(e))
                time.sleep(60)

async def main():
    await program()
asyncio.run(main())