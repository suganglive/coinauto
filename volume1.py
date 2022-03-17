import pyupbit
import operator
import pandas as pd
import numpy as np

def get_tickers():
    tickers = pyupbit.get_tickers("KRW")
    dct = {}

    for tick in tickers:
        data = pyupbit.get_ohlcv(tick, count=6)
        try:
            vol1 = data['volume'].rolling(window=5).mean()
            close = data['close'].rolling(window=5).mean()
            vol2 = vol1 * close
            print(vol2)
            dct[tick] = vol2[-2]
            print(dct[tick])
        except:
            print(f"{tick}_error")

    sorted_d = dict(sorted(dct.items(), key=operator.itemgetter(1), reverse=True))
    a = list(sorted_d.keys())[:5]
    return a

print(get_tickers())