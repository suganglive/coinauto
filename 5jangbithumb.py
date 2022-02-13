import pyupbit
import time

# tickers = pyupbit.get_tickers()
# print(tickers)

# detail = pyupbit.get_ohlcv("KRW-BTC", interval = "day", count=1)
# print(detail)

# orderbook = pyupbit.get_orderbook("KRW-BTC")

# for i in orderbook:
#     print(i)

# all = pyupbit.get_current_price()
# for i, l in all.items():
#     print(i, l)

krw = pyupbit.get_tickers(fiat="KRW")

for i in krw:
    a = pyupbit.get_ohlcv(i, interval="day", count=1)
    print(i, a)
    