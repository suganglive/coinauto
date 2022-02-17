import ccxt
from datetime import datetime

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[2].strip()
    secret_key = lines[3].strip()
    binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

# balance = binance.fetch_balance()
# print(balance['BTC'])


# ohlcvs = binance.fetch_ohlcv("BTC/USDT", timeframe='1d')

# for ohlc in ohlcvs:
#     print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'))

# orderbook = binance.fetch_order_book("BTC/USDT")
# print(orderbook)
# for ask in orderbook['asks']:
#     print(ask[0], ask[1])