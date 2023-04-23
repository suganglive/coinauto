import requests
import pandas as pd
import re
from requests import Response
from typing import Any, Tuple, Dict, Optional
from errors import error_handler, RemainingReqParsingError
import time
import datetime


HTTP_RESP_CODE_START = 200
HTTP_RESP_CODE_END = 400

def _parse(remaining_req: str) -> Dict[str, Any]:
    """Parse the number of remaining requests info for Upbit API
    Args:
        remaining_req (str): String of the number of remaining requests info
         like "group=market; min=573; sec=9"
    Returns:
        Parsed dictionary of the number of remaining requests info
         like {'group': 'market', 'min': 573, 'sec': 2}
    Raises:
        RemainingReqParsingError: If the input can not be parsed.
    """
    try:
        pattern = re.compile(r"group=([a-z\-]+); min=([0-9]+); sec=([0-9]+)")
        matched = pattern.search(remaining_req)
        if matched is None:
            raise RemainingReqParsingError

        ret = {
            "group": matched.group(1),
            "min": int(matched.group(2)),
            "sec": int(matched.group(3)),
        }
        return ret
    except (AttributeError, ValueError):
        raise 

@error_handler
def _call_get(url: str, **kwargs: Any) -> Response:
    return requests.get(url, **kwargs)

def _call_public_api(url: str, **params: Any) -> Tuple[Any, Dict[str, Any]]:
    """Call Upbit public api
    Args:
        url (str): REST API url
        params (any): GET method parameters
    Returns:
        The contents of requested url, parsed remaining requests count info
    """
    resp = _call_get(url, params=params)
    data = resp.json()
    remaining_req = resp.headers.get("Remaining-Req", "")
    limit = _parse(remaining_req)
    return data, limit


def get_ohlcv(ticker="KRW-BTC", interval="day", count=200, to=None,
              period=0.1):
    MAX_CALL_COUNT = 200
    try:
        url = "https://api.upbit.com/v1/candles/minutes/60"
        to = datetime.datetime.now()

        dfs = []
        count = max(count, 1)
        for pos in range(count, 0, -200):
            query_count = min(MAX_CALL_COUNT, pos)

            to = to.strftime("%Y-%m-%d %H:%M:%S")

            contents, _ = _call_public_api(
                url, market=ticker, count=query_count, to=to)

            dt_list = []
            for x in contents:
                dt = datetime.datetime.strptime(
                    x['candle_date_time_kst'], "%Y-%m-%dT%H:%M:%S")
                #dt_list.append(dt.astimezone())
                dt_list.append(dt)

            df = pd.DataFrame(contents,
                              columns=[
                                  'opening_price',
                                  'high_price',
                                  'low_price',
                                  'trade_price',
                                  'candle_acc_trade_volume',
                                  'candle_acc_trade_price'],
                              index=dt_list)
            df = df.sort_index()
            if df.shape[0] == 0:
                break
            dfs += [df]

            to = datetime.datetime.strptime(
                contents[-1]['candle_date_time_utc'], "%Y-%m-%dT%H:%M:%S")

            if pos > 200:
                time.sleep(period)

        df = pd.concat(dfs).sort_index()
        df = df.rename(columns={"opening_price": "open",
                                "high_price": "high",
                                "low_price": "low",
                                "trade_price": "close",
                                "candle_acc_trade_volume": "volume",
                                "candle_acc_trade_price": "value"})
        return df
    except Exception:
        return None

def get_daily_ohlcv_from_base(ticker="KRW-BTC", base='0h', count=200):
    try:
        df = get_ohlcv(ticker, interval="minute60", count=count)
        df = df.resample('24H', offset=base).agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        })
        return df
    except Exception:
        return None
