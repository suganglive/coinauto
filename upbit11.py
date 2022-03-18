#upbit 11, mum account, k 0.8, v = 0.2, amount = 1.12, m = 10
import pyupbit
import time
import datetime
import logging
import pyupbase as pb
import uprank20 as rk

logging.basicConfig(filename='upbit11.log', level=logging.INFO, format='%(asctime)s:%(message)s')

access_key = "a"
secret_key = "b"
upbit = pyupbit.Upbit(access_key, secret_key)

# with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
#     lines = f.readlines()
#     access_key = lines[8].strip()
#     secret_key = lines[9].strip()
#     upbit = pyupbit.Upbit(access_key, secret_key)

tickers = rk.get_tickers()
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

k = 0.8
target_v = 0.2
m = 10
amount = 20

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
        percentage = 1/amount
    else:
        percentage = (1/amount)*(target_v/range_ratio)
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
    df = pb.get_daily_ohlcv_from_base(ticker = ticker, count = m*24)
    open = df['open']
    ma = open.rolling(window=m).mean()
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

        coin6_open = get_open(coin6)
        coin6_ma5 = get_ma5(coin6)
        coin6_target = get_target_price(coin6)
        coin6_percent = get_percentage(coin6)
        coin6_status = 0

        coin7_open = get_open(coin7)
        coin7_ma5 = get_ma5(coin7)
        coin7_target = get_target_price(coin7)
        coin7_percent = get_percentage(coin7)
        coin7_status = 0

        coin8_open = get_open(coin8)
        coin8_ma5 = get_ma5(coin8)
        coin8_target = get_target_price(coin8)
        coin8_percent = get_percentage(coin8)
        coin8_status = 0

        coin9_open = get_open(coin9)
        coin9_ma5 = get_ma5(coin9)
        coin9_target = get_target_price(coin9)
        coin9_percent = get_percentage(coin9)
        coin9_status = 0

        coin10_open = get_open(coin10)
        coin10_ma5 = get_ma5(coin10)
        coin10_target = get_target_price(coin10)
        coin10_percent = get_percentage(coin10)
        coin10_status = 0

        coin11_open = get_open(coin11)
        coin11_ma5 = get_ma5(coin11)
        coin11_target = get_target_price(coin11)
        coin11_percent = get_percentage(coin11)
        coin11_status = 0

        coin12_open = get_open(coin12)
        coin12_ma5 = get_ma5(coin12)
        coin12_target = get_target_price(coin12)
        coin12_percent = get_percentage(coin12)
        coin12_status = 0

        coin13_open = get_open(coin13)
        coin13_ma5 = get_ma5(coin13)
        coin13_target = get_target_price(coin13)
        coin13_percent = get_percentage(coin13)
        coin13_status = 0

        coin14_open = get_open(coin14)
        coin14_ma5 = get_ma5(coin14)
        coin14_target = get_target_price(coin14)
        coin14_percent = get_percentage(coin14)
        coin14_status = 0

        coin15_open = get_open(coin15)
        coin15_ma5 = get_ma5(coin15)
        coin15_target = get_target_price(coin15)
        coin15_percent = get_percentage(coin15)
        coin15_status = 0

        coin16_open = get_open(coin16)
        coin16_ma5 = get_ma5(coin16)
        coin16_target = get_target_price(coin16)
        coin16_percent = get_percentage(coin16)
        coin16_status = 0

        coin17_open = get_open(coin17)
        coin17_ma5 = get_ma5(coin17)
        coin17_target = get_target_price(coin17)
        coin17_percent = get_percentage(coin17)
        coin17_status = 0

        coin18_open = get_open(coin18)
        coin18_ma5 = get_ma5(coin18)
        coin18_target = get_target_price(coin18)
        coin18_percent = get_percentage(coin18)
        coin18_status = 0

        coin19_open = get_open(coin19)
        coin19_ma5 = get_ma5(coin19)
        coin19_target = get_target_price(coin19)
        coin19_percent = get_percentage(coin19)
        coin19_status = 0

        coin20_open = get_open(coin20)
        coin20_ma5 = get_ma5(coin20)
        coin20_target = get_target_price(coin20)
        coin20_percent = get_percentage(coin20)
        coin20_status = 0

        krw = upbit.get_balance("KRW")
        krw = round(krw)
        logging.info(f"coin1 = {coin1}, coin1_percent = {coin1_percent}, coin1_open : {coin1_open}, coin1_ma5 : {coin1_ma5}, coin1_target : {coin1_target}, coin1_status : {coin1_status}")
        logging.info(f"coin2 = {coin2}, coin2_percent = {coin2_percent}, coin2_open : {coin2_open}, coin2_ma5 : {coin2_ma5}, coin2_target : {coin2_target}, coin2_status : {coin2_status}")
        logging.info(f"coin3 = {coin3}, coin3_percent = {coin3_percent}, coin3_open : {coin3_open}, coin3_ma5 : {coin3_ma5}, coin3_target : {coin3_target}, coin3_status : {coin3_status}")
        logging.info(f"coin4 = {coin4}, coin4_percent = {coin4_percent}, coin4_open : {coin4_open}, coin4_ma5 : {coin4_ma5}, coin4_target : {coin4_target}, coin4_status : {coin4_status}")
        logging.info(f"coin5 = {coin5}, coin5_percent = {coin5_percent}, coin5_open : {coin5_open}, coin5_ma5 : {coin5_ma5}, coin5_target : {coin5_target}, coin5_status : {coin5_status}")
        logging.info(f"coin6 = {coin6}, coin6_percent = {coin6_percent}, coin6_open : {coin6_open}, coin6_ma5 : {coin6_ma5}, coin6_target : {coin6_target}, coin6_status : {coin6_status}")
        logging.info(f"coin7 = {coin7}, coin7_percent = {coin7_percent}, coin7_open : {coin7_open}, coin7_ma5 : {coin7_ma5}, coin7_target : {coin7_target}, coin7_status : {coin7_status}")
        logging.info(f"coin8 = {coin8}, coin8_percent = {coin8_percent}, coin8_open : {coin8_open}, coin8_ma5 : {coin8_ma5}, coin8_target : {coin8_target}, coin8_status : {coin8_status}")
        logging.info(f"coin9 = {coin9}, coin9_percent = {coin9_percent}, coin9_open : {coin9_open}, coin9_ma5 : {coin9_ma5}, coin9_target : {coin9_target}, coin9_status : {coin9_status}")
        logging.info(f"coin10 = {coin10}, coin10_percent = {coin10_percent}, coin10_open : {coin10_open}, coin10_ma5 : {coin10_ma5}, coin10_target : {coin10_target}, coin10_status : {coin10_status}")
        logging.info(f"coin11 = {coin11}, coin11_percent = {coin11_percent}, coin11_open : {coin11_open}, coin11_ma5 : {coin11_ma5}, coin11_target : {coin11_target}, coin11_status : {coin11_status}")
        logging.info(f"coin12 = {coin12}, coin12_percent = {coin12_percent}, coin12_open : {coin12_open}, coin12_ma5 : {coin12_ma5}, coin12_target : {coin12_target}, coin12_status : {coin12_status}")
        logging.info(f"coin13 = {coin13}, coin13_percent = {coin13_percent}, coin13_open : {coin13_open}, coin13_ma5 : {coin13_ma5}, coin13_target : {coin13_target}, coin13_status : {coin13_status}")
        logging.info(f"coin14 = {coin14}, coin14_percent = {coin14_percent}, coin14_open : {coin14_open}, coin14_ma5 : {coin14_ma5}, coin14_target : {coin14_target}, coin14_status : {coin14_status}")
        logging.info(f"coin15 = {coin15}, coin15_percent = {coin15_percent}, coin15_open : {coin15_open}, coin15_ma5 : {coin15_ma5}, coin15_target : {coin15_target}, coin15_status : {coin15_status}")
        logging.info(f"coin16 = {coin16}, coin16_percent = {coin16_percent}, coin16_open : {coin16_open}, coin16_ma5 : {coin16_ma5}, coin16_target : {coin16_target}, coin16_status : {coin16_status}")
        logging.info(f"coin17 = {coin17}, coin17_percent = {coin17_percent}, coin17_open : {coin17_open}, coin17_ma5 : {coin17_ma5}, coin17_target : {coin17_target}, coin17_status : {coin17_status}")
        logging.info(f"coin18 = {coin18}, coin18_percent = {coin18_percent}, coin18_open : {coin18_open}, coin18_ma5 : {coin18_ma5}, coin18_target : {coin18_target}, coin18_status : {coin18_status}")
        logging.info(f"coin19 = {coin19}, coin19_percent = {coin19_percent}, coin19_open : {coin19_open}, coin19_ma5 : {coin19_ma5}, coin19_target : {coin19_target}, coin19_status : {coin19_status}")
        logging.info(f"coin20 = {coin20}, coin20_percent = {coin20_percent}, coin20_open : {coin20_open}, coin20_ma5 : {coin20_ma5}, coin20_target : {coin20_target}, coin20_status : {coin20_status}")
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
            tickers = rk.get_tickers()
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

            coin1_percent = get_percentage(coin1)
            coin2_percent = get_percentage(coin2)
            coin3_percent = get_percentage(coin3)
            coin4_percent = get_percentage(coin4)
            coin5_percent = get_percentage(coin5)
            coin6_percent = get_percentage(coin6)
            coin7_percent = get_percentage(coin7)
            coin8_percent = get_percentage(coin8)
            coin9_percent = get_percentage(coin9)
            coin10_percent = get_percentage(coin10)
            coin11_percent = get_percentage(coin11)
            coin12_percent = get_percentage(coin12)
            coin13_percent = get_percentage(coin13)
            coin14_percent = get_percentage(coin14)
            coin15_percent = get_percentage(coin15)
            coin16_percent = get_percentage(coin16)
            coin17_percent = get_percentage(coin17)
            coin18_percent = get_percentage(coin18)
            coin19_percent = get_percentage(coin19)
            coin20_percent = get_percentage(coin20)
            
            coin1_target = get_target_price(coin1)
            coin2_target = get_target_price(coin2)
            coin3_target = get_target_price(coin3)
            coin4_target = get_target_price(coin4)
            coin5_target = get_target_price(coin5)
            coin6_target = get_target_price(coin6)
            coin7_target = get_target_price(coin7)
            coin8_target = get_target_price(coin8)
            coin9_target = get_target_price(coin9)
            coin10_target = get_target_price(coin10)
            coin11_target = get_target_price(coin11)
            coin12_target = get_target_price(coin12)
            coin13_target = get_target_price(coin13)
            coin14_target = get_target_price(coin14)
            coin15_target = get_target_price(coin15)
            coin16_target = get_target_price(coin16)
            coin17_target = get_target_price(coin17)
            coin18_target = get_target_price(coin18)
            coin19_target = get_target_price(coin19)
            coin20_target = get_target_price(coin20)

            coin1_ma5 = get_ma5(coin1)
            coin2_ma5 = get_ma5(coin2)
            coin3_ma5 = get_ma5(coin3)
            coin4_ma5 = get_ma5(coin4)
            coin5_ma5 = get_ma5(coin5)
            coin6_ma5 = get_ma5(coin6)
            coin7_ma5 = get_ma5(coin7)
            coin8_ma5 = get_ma5(coin8)
            coin9_ma5 = get_ma5(coin9)
            coin10_ma5 = get_ma5(coin10)
            coin11_ma5 = get_ma5(coin11)
            coin12_ma5 = get_ma5(coin12)
            coin13_ma5 = get_ma5(coin13)
            coin14_ma5 = get_ma5(coin14)
            coin15_ma5 = get_ma5(coin15)
            coin16_ma5 = get_ma5(coin16)
            coin17_ma5 = get_ma5(coin17)
            coin18_ma5 = get_ma5(coin18)
            coin19_ma5 = get_ma5(coin19)
            coin20_ma5 = get_ma5(coin20)

            coin1_open = get_open(coin1)
            coin2_open = get_open(coin2)
            coin3_open = get_open(coin3)
            coin4_open = get_open(coin4)
            coin5_open = get_open(coin5)
            coin6_open = get_open(coin6)
            coin7_open = get_open(coin7)
            coin8_open = get_open(coin8)
            coin9_open = get_open(coin9)
            coin10_open = get_open(coin10)
            coin11_open = get_open(coin11)
            coin12_open = get_open(coin12)
            coin13_open = get_open(coin13)
            coin14_open = get_open(coin14)
            coin15_open = get_open(coin15)
            coin16_open = get_open(coin16)
            coin17_open = get_open(coin17)
            coin18_open = get_open(coin18)
            coin19_open = get_open(coin19)
            coin20_open = get_open(coin20)
            
            coin1_status = 0
            coin2_status = 0
            coin3_status = 0
            coin4_status = 0
            coin5_status = 0
            coin6_status = 0
            coin7_status = 0
            coin8_status = 0
            coin9_status = 0
            coin10_status = 0
            coin11_status = 0
            coin12_status = 0
            coin13_status = 0
            coin14_status = 0
            coin15_status = 0
            coin16_status = 0
            coin17_status = 0
            coin18_status = 0
            coin19_status = 0
            coin20_status = 0

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
            logging.info(f"coin6 = {coin6}, coin6_percent = {coin6_percent}, coin6_open : {coin6_open}, coin6_ma5 : {coin6_ma5}, coin6_target : {coin6_target}, coin6_status : {coin6_status}")
            logging.info(f"coin7 = {coin7}, coin7_percent = {coin7_percent}, coin7_open : {coin7_open}, coin7_ma5 : {coin7_ma5}, coin7_target : {coin7_target}, coin7_status : {coin7_status}")
            logging.info(f"coin8 = {coin8}, coin8_percent = {coin8_percent}, coin8_open : {coin8_open}, coin8_ma5 : {coin8_ma5}, coin8_target : {coin8_target}, coin8_status : {coin8_status}")
            logging.info(f"coin9 = {coin9}, coin9_percent = {coin9_percent}, coin9_open : {coin9_open}, coin9_ma5 : {coin9_ma5}, coin9_target : {coin9_target}, coin9_status : {coin9_status}")
            logging.info(f"coin10 = {coin10}, coin10_percent = {coin10_percent}, coin10_open : {coin10_open}, coin10_ma5 : {coin10_ma5}, coin10_target : {coin10_target}, coin10_status : {coin10_status}")
            logging.info(f"coin11 = {coin11}, coin11_percent = {coin11_percent}, coin11_open : {coin11_open}, coin11_ma5 : {coin11_ma5}, coin11_target : {coin11_target}, coin11_status : {coin11_status}")
            logging.info(f"coin12 = {coin12}, coin12_percent = {coin12_percent}, coin12_open : {coin12_open}, coin12_ma5 : {coin12_ma5}, coin12_target : {coin12_target}, coin12_status : {coin12_status}")
            logging.info(f"coin13 = {coin13}, coin13_percent = {coin13_percent}, coin13_open : {coin13_open}, coin13_ma5 : {coin13_ma5}, coin13_target : {coin13_target}, coin13_status : {coin13_status}")
            logging.info(f"coin14 = {coin14}, coin14_percent = {coin14_percent}, coin14_open : {coin14_open}, coin14_ma5 : {coin14_ma5}, coin14_target : {coin14_target}, coin14_status : {coin14_status}")
            logging.info(f"coin15 = {coin15}, coin15_percent = {coin15_percent}, coin15_open : {coin15_open}, coin15_ma5 : {coin15_ma5}, coin15_target : {coin15_target}, coin15_status : {coin15_status}")
            logging.info(f"coin16 = {coin16}, coin16_percent = {coin16_percent}, coin16_open : {coin16_open}, coin16_ma5 : {coin16_ma5}, coin16_target : {coin16_target}, coin16_status : {coin16_status}")
            logging.info(f"coin17 = {coin17}, coin17_percent = {coin17_percent}, coin17_open : {coin17_open}, coin17_ma5 : {coin17_ma5}, coin17_target : {coin17_target}, coin17_status : {coin17_status}")
            logging.info(f"coin18 = {coin18}, coin18_percent = {coin18_percent}, coin18_open : {coin18_open}, coin18_ma5 : {coin18_ma5}, coin18_target : {coin18_target}, coin18_status : {coin18_status}")
            logging.info(f"coin19 = {coin19}, coin19_percent = {coin19_percent}, coin19_open : {coin19_open}, coin19_ma5 : {coin19_ma5}, coin19_target : {coin19_target}, coin19_status : {coin19_status}")
            logging.info(f"coin20 = {coin20}, coin20_percent = {coin20_percent}, coin20_open : {coin20_open}, coin20_ma5 : {coin20_ma5}, coin20_target : {coin20_target}, coin20_status : {coin20_status}")
            logging.info(f"krw_balance : {krw}")

        coin1_current_price = pyupbit.get_current_price(coin1)
        coin2_current_price = pyupbit.get_current_price(coin2)
        coin3_current_price = pyupbit.get_current_price(coin3)
        coin4_current_price = pyupbit.get_current_price(coin4)
        coin5_current_price = pyupbit.get_current_price(coin5)
        coin6_current_price = pyupbit.get_current_price(coin6)
        coin7_current_price = pyupbit.get_current_price(coin7)
        coin8_current_price = pyupbit.get_current_price(coin8)
        coin9_current_price = pyupbit.get_current_price(coin9)
        coin10_current_price = pyupbit.get_current_price(coin10)
        coin11_current_price = pyupbit.get_current_price(coin11)
        coin12_current_price = pyupbit.get_current_price(coin12)
        coin13_current_price = pyupbit.get_current_price(coin13)
        coin14_current_price = pyupbit.get_current_price(coin14)
        coin15_current_price = pyupbit.get_current_price(coin15)
        coin16_current_price = pyupbit.get_current_price(coin16)
        coin17_current_price = pyupbit.get_current_price(coin17)
        coin18_current_price = pyupbit.get_current_price(coin18)
        coin19_current_price = pyupbit.get_current_price(coin19)
        coin20_current_price = pyupbit.get_current_price(coin20)
        
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

        if coin6_current_price > coin6_target and coin6_status == 0 and coin6_open > coin6_ma5:
            try:
                buy_limit(coin6, krw)
                
                coin6_status = 1
                logging.info("coin6 get")
            except Exception as e:
                logging.info("coin6 buy error", str(e))
        
        if coin7_current_price > coin7_target and coin7_status == 0 and coin7_open > coin7_ma5:
            try:
                buy_limit(coin7, krw)
                
                coin7_status = 1
                logging.info("coin7 get")
            except Exception as e:
                logging.info("coin7 buy error", str(e))
        
        if coin8_current_price > coin8_target and coin8_status == 0 and coin8_open > coin8_ma5:
            try:
                buy_limit(coin8, krw)
                
                coin8_status = 1
                logging.info("coin8 get")
            except Exception as e:
                logging.info("coin8 buy error", str(e))

        if coin9_current_price > coin9_target and coin9_status == 0 and coin9_open > coin9_ma5:
            try:
                buy_limit(coin9, krw)
                
                coin9_status = 1
                logging.info("coin9 get")
            except Exception as e:
                logging.info("coin9 buy error", str(e))

        if coin10_current_price > coin10_target and coin10_status == 0 and coin10_open > coin10_ma5:
            try:
                buy_limit(coin10, krw)
                
                coin10_status = 1
                logging.info("coin10 get")
            except Exception as e:
                logging.info("coin10 buy error", str(e))

        if coin11_current_price > coin11_target and coin11_status == 0 and coin11_open > coin11_ma5:
            try:
                buy_limit(coin11, krw)
                
                coin11_status = 1
                logging.info("coin11 get")
            except Exception as e:
                logging.info("coin11 buy error", str(e))

        if coin12_current_price > coin12_target and coin12_status == 0 and coin12_open > coin12_ma5:
            try:
                buy_limit(coin12, krw)
                
                coin12_status = 1
                logging.info("coin12 get")
            except Exception as e:
                logging.info("coin12 buy error", str(e))

        if coin13_current_price > coin13_target and coin13_status == 0 and coin13_open > coin13_ma5:
            try:
                buy_limit(coin13, krw)
                
                coin13_status = 1
                logging.info("coin13 get")
            except Exception as e:
                logging.info("coin13 buy error", str(e))

        if coin14_current_price > coin14_target and coin14_status == 0 and coin14_open > coin14_ma5:
            try:
                buy_limit(coin14, krw)
                
                coin14_status = 1
                logging.info("coin14 get")
            except Exception as e:
                logging.info("coin14 buy error", str(e))

        if coin15_current_price > coin15_target and coin15_status == 0 and coin15_open > coin15_ma5:
            try:
                buy_limit(coin15, krw)
                
                coin15_status = 1
                logging.info("coin15 get")
            except Exception as e:
                logging.info("coin15 buy error", str(e))

        if coin16_current_price > coin16_target and coin16_status == 0 and coin16_open > coin16_ma5:
            try:
                buy_limit(coin16, krw)
                
                coin16_status = 1
                logging.info("coin16 get")
            except Exception as e:
                logging.info("coin16 buy error", str(e))

        if coin17_current_price > coin17_target and coin17_status == 0 and coin17_open > coin17_ma5:
            try:
                buy_limit(coin17, krw)
                
                coin17_status = 1
                logging.info("coin17 get")
            except Exception as e:
                logging.info("coin17 buy error", str(e))

        if coin18_current_price > coin18_target and coin18_status == 0 and coin18_open > coin18_ma5:
            try:
                buy_limit(coin18, krw)
                
                coin18_status = 1
                logging.info("coin18 get")
            except Exception as e:
                logging.info("coin18 buy error", str(e))

        if coin19_current_price > coin19_target and coin19_status == 0 and coin19_open > coin19_ma5:
            try:
                buy_limit(coin19, krw)
                
                coin19_status = 1
                logging.info("coin19 get")
            except Exception as e:
                logging.info("coin19 buy error", str(e))

        if coin20_current_price > coin20_target and coin20_status == 0 and coin20_open > coin20_ma5:
            try:
                buy_limit(coin20, krw)
                
                coin20_status = 1
                logging.info("coin20 get")
            except Exception as e:
                logging.info("coin20 buy error", str(e))
        
    except Exception as e:
        logging.info("programm error : " + str(e))
    time.sleep(1)