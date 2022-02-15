from decimal import ROUND_CEILING, ROUND_UP
import pyupbit
import time
import datetime
import math

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

xrp_orderbook = pyupbit.get_orderbook("KRW-XRP")
xrp_price = xrp_orderbook["orderbook_units"][0]['ask_price']
print(xrp_price)
