import pyupbit
import numpy as np
import pandas as pd
import time

def get_daily_ohlcv_from_base(ticker="KRW-BTC", base='11h', count = 144):
    """
    :param ticker:
    :param base:
    :return:
    """
    try:
        df = pyupbit.get_ohlcv(ticker, interval="minute60", count = count)
        df = df.resample('24H', offset=base).agg(
            {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'})
        # time.sleep(1)
        return df
    except Exception as e:
        print("pyupbase", e)
        return None

# print(get_daily_ohlcv_from_base())