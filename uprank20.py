import upbit
import operator
import upbase as pb

def get_ranks(base):
    tickers = upbit.get_tickers()
    dct = {}

    for tick in tickers:
        data = pb.get_daily_ohlcv_from_base(ticker = tick, base=base)
        try:
            vol1 = data['volume'].rolling(window=5).mean()
            close = data['close'].rolling(window=5).mean()
            vol2 = vol1 * close
            dct[tick] = vol2[-2]
        except:
            pass
            
    sorted_d = dict(sorted(dct.items(), key=operator.itemgetter(1), reverse=True))
    a = list(sorted_d.keys())[:20]
    a = list(sorted_d.keys())[:2]
    return a
