import pyupbit
import time
import datetime
import logging
import pyupbase as pb
import uprank20_2 as rk
import math

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[1].strip()
    secret_key = lines[2].strip()
    upbit = pyupbit.Upbit(access_key, secret_key)

print(upbit.get_balance("KRW",))