import pyupbit
import time
import datetime
import logging
import pyupbase as pb
import uprank20 as rk

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[1].strip()
    secret_key = lines[2].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

# ret = upbit.cancel_order()
# print(upbit.get_balance("KRW"))
# print(upbit.get_order("KRW-BTC"))
# a = upbit.get_order("KRW-BTC")
# print(a[0]['uuid'])
# upbit.cancel_order(a[0]['uuid'])

if upbit.get_order("KRW-XRP"):
    print('yes')
else:
    print('no')