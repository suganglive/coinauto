import pyupbit
import operator
import pandas as pd
import numpy as np
import pyupbase as pb
import time

def get_tickers(base):
    tickers = pyupbit.get_tickers("KRW")
    dct = {}

    for tick in tickers:
        data = pb.get_daily_ohlcv_from_base(ticker = tick, base=base)
        try:
            vol1 = data['volume'].rolling(window=5).mean()
            close = data['close'].rolling(window=5).mean()
            vol2 = vol1 * close
            # print(vol2)
            dct[tick] = vol2[-2]
            # print(dct[tick])
            time.sleep(0.05)
        except:
            print(f"{tick}_error")

    sorted_d = dict(sorted(dct.items(), key=operator.itemgetter(1), reverse=True))
    # a = list(sorted_d.keys())[:20]
    a = list(sorted_d.keys())[:2]
    return a
