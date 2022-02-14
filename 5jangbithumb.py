import pyupbit

def sma5(ticker):
    df = pyupbit.get_ohlcv(ticker)
    ma5 = df["close"].rolling(window=5).mean()
    last_ma5 = ma5[-2]
    price = pyupbit.get_current_price(ticker)

    if price > last_ma5:
        return True
    else:
        return False
        
tickers = pyupbit.get_tickers(fiat="KRW")

for i in tickers:
    bull = sma5(i)
    if bull:
        print(i, "is bull market")
    else:
        print(i, "is bear market")