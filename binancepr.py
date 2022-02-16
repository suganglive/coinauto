import ccxt
from datetime import datetime

binance = ccxt.binance()
# ohlcvs = binance.fetch_ohlcv("BTC/USDT", timeframe='1d')

# for ohlc in ohlcvs:
#     print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'))

orderbook = binance.fetch_order_book("BTC/USDT")
print(orderbook)
# for ask in orderbook['asks']:
#     print(ask[0], ask[1])