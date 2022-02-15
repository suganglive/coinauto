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

# a = pyupbit.get_current_price("KRW-BTC")
# print(a)
# a = a * 1.002
# print(a)
# a = a/1000
# a = math.ceil(a)
# a = a * 1000
# print(a)

# btc_current_price = pyupbit.get_current_price("KRW-BTC")
# btc_price = btc_current_price * 1.002
# btc_price = btc_price/1000
# math.ceil(btc_price)
# btc_price = btc_price * 1000
# print(btc_price)

a = 1
b = 2
c = 3
d = 4

if (d > c) and (b > c):
    print("yes")
else:
    print("no")