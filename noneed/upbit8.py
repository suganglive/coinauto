#10시 기준, k=0.5, v=0.05
# 업비트, 상승장, 변동성 돌파, 변동성 조절 Coins : [BTC, ETH, XRP, LTC], 11시 초기화, 로그파일생성, 11시 체결 여부 확인, 모든 함수 재사용 가능
# nohup python3 upbit8.py > output.log &
import pyupbit
import time
import datetime
import math
import logging
import pyupbase as pb

logging.basicConfig(filename='upbit8.log', level=logging.INFO, format='%(asctime)s:%(message)s')

access_key = "a"
secret_key = "b"
upbit = pyupbit.Upbit(access_key, secret_key)

# with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
#     lines = f.readlines()
#     access_key = lines[0].strip()
#     secret_key = lines[1].strip()
#     upbit = pyupbit.Upbit(access_key, secret_key)

tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-LTC"]
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
        percentage = 1/4
    else:
        percentage = (1/4)*(target_v/range_ratio)
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
    target = get_target_price(ticker)
    if target - 1 < 0:
        if target * 10 - 1 < 0:
            target = target * 10000
            target = math.floor(target)
            target = target + 1
            target = target / 10000
        else:
            target = target * 1000
            target = math.floor(target)
            target = target + 1
            target = target / 1000
    elif len(str(math.floor(target))) == 1:
        target = target * 100
        target = math.floor(target)
        target = target + 1
        target = target / 100
    elif len(str(math.floor(target))) == 2:
        target = target * 10
        target = math.floor(target)
        target = target + 1
        target = target / 10
    elif len(str(math.floor(target))) == 3:
        target = math.floor(target)
        target = target + 1
    elif len(str(math.floor(target))) == 4:
        if target % 10 <= 5: 
            target = target / 10
            target = math.floor(target)
            target = target * 10
            target = target + 5
        else:
            target = target / 10
            target = math.floor(target)
            target = target * 10
            target = target + 10
    elif len(str(math.floor(target))) == 5:
        target = math.floor(target)
        target = target + 10
    elif len(str(math.floor(target))) == 6:
        if (target/10) % 10 <= 5: 
            target = target / 100
            target = math.floor(target)
            target = target * 100
            target = target + 50
        else:
            target = target / 100
            target = math.floor(target)
            target = target * 100
            target = target + 100
    elif len(str(math.floor(target))) >=7:
        target = target / 1000
        target = math.floor(target)
        target = target * 1000
        target = target + 1000
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
    price = sell_price(ticker)
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
        btc_open = get_open("KRW-BTC")
        btc_ma5 = get_ma5("KRW-BTC")
        btc_target = get_target_price("KRW-BTC")
        btc_percent = get_percentage("KRW-BTC")
        btc_status = 0

        eth_open = get_open("KRW-ETH")
        eth_ma5 = get_ma5("KRW-ETH")
        eth_target = get_target_price("KRW-ETH")
        eth_percent = get_percentage("KRW-ETH")
        eth_status = 0

        xrp_open = get_open("KRW-XRP")
        xrp_ma5 = get_ma5("KRW-XRP")
        xrp_target = get_target_price("KRW-XRP")
        xrp_percent = get_percentage("KRW-XRP")
        xrp_status = 0

        ltc_open = get_open("KRW-LTC")
        ltc_ma5 = get_ma5("KRW-LTC")
        ltc_target = get_target_price("KRW-LTC")
        ltc_percent = get_percentage("KRW-LTC")
        ltc_status = 0

        krw = upbit.get_balance("KRW")
        krw = round(krw)
        logging.info(f"btc_percent = {btc_percent}, btc_open : {btc_open}, btc_ma5 : {btc_ma5}, btc_target : {btc_target}, btc_status : {btc_status}")
        logging.info(f"eth_percent = {eth_percent}, eth_open : {eth_open}, eth_ma5 : {eth_ma5}, eth_target : {eth_target}, eth_status : {eth_status}")
        logging.info(f"xrp_percent = {xrp_percent}, xrp_open : {xrp_open}, xrp_ma5 : {xrp_ma5}, xrp_target : {xrp_target}, xrp_status : {xrp_status}")
        logging.info(f"ltc_percent = {ltc_percent}, ltc_open : {ltc_open}, ltc_ma5 : {ltc_ma5}, ltc_target : {ltc_target}, ltc_status : {ltc_status}")
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
            btc_percent = get_percentage("KRW-BTC")
            eth_percent = get_percentage("KRW-ETH")
            xrp_percent = get_percentage("KRW-XRP")
            ltc_percent = get_percentage("KRW-LTC")
            btc_target = get_target_price("KRW-BTC")
            eth_target = get_target_price("KRW-ETH")
            xrp_target = get_target_price("KRW-XRP")
            ltc_target = get_target_price("KRW-LTC")
            btc_ma5 = get_ma5("KRW-BTC")
            eth_ma5 = get_ma5("KRW-ETH")
            xrp_ma5 = get_ma5("KRW-XRP")
            ltc_ma5 = get_ma5("KRW-LTC")
            btc_open = get_open("KRW-BTC")
            eth_open = get_open("KRW-ETH")
            xrp_open = get_open("KRW-XRP")
            ltc_open = get_open("KRW-LTC")
            btc_status = 0
            eth_status = 0
            xrp_status = 0
            ltc_status = 0
            krw1 = upbit.get_balance("KRW")
            profit = krw1/krw -1
            logging.info(f"profit : {profit}")
            krw = upbit.get_balance("KRW")
            krw = round(krw)
            ten = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1, hours=10)
            logging.info(f"btc_percent = {btc_percent}, btc_open : {btc_open}, btc_ma5 : {btc_ma5}, btc_target : {btc_target}, btc_status : {btc_status}")
            logging.info(f"eth_percent = {eth_percent}, eth_open : {eth_open}, eth_ma5 : {eth_ma5}, eth_target : {eth_target}, eth_status : {eth_status}")
            logging.info(f"xrp_percent = {xrp_percent}, xrp_open : {xrp_open}, xrp_ma5 : {xrp_ma5}, xrp_target : {xrp_target}, xrp_status : {xrp_status}")
            logging.info(f"ltc_percent = {ltc_percent}, ltc_open : {ltc_open}, ltc_ma5 : {ltc_ma5}, ltc_target : {ltc_target}, ltc_status : {ltc_status}")
            logging.info(f"krw_balance : {krw}")

        btc_current_price = pyupbit.get_current_price("KRW-BTC")
        eth_current_price = pyupbit.get_current_price("KRW-ETH")
        xrp_current_price = pyupbit.get_current_price("KRW-XRP")
        ltc_current_price = pyupbit.get_current_price("KRW-LTC")
        
        if btc_current_price > btc_target and btc_status == 0 and btc_open > btc_ma5:
            try:
                buy_limit("KRW-BTC", krw)
                btc_status = 1
                logging.info("btc get")
            except Exception as e:
                logging.info("btc buy error", str(e))

        if eth_current_price > eth_target and eth_status == 0 and eth_open > eth_ma5:
            try:
                buy_limit("KRW-ETH", krw)
                eth_status = 1
                logging.info("eth get")
            except Exception as e:
                logging.info("eth buy error", str(e))

        if xrp_current_price > xrp_target and xrp_status == 0 and xrp_open > xrp_ma5:
            try:
                buy_limit("KRW-XRP", krw)
                xrp_status = 1
                logging.info("xrp get")
            except Exception as e:
                logging.info("xrp buy error", str(e))

        if ltc_current_price > ltc_target and ltc_status == 0 and ltc_open > ltc_ma5:
            try:
                buy_limit("KRW-LTC", krw)
                ltc_status = 1
                logging.info("ltc get")
            except Exception as e:
                logging.info("ltc buy error", str(e))
        
    except Exception as e:
        logging.info("programm error : " + str(e))
    time.sleep(1)