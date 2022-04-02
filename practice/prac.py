import pyupbit
import time
import datetime
import logging
import pyupbase as pb
import uprank20_2 as rk
import math

a = pyupbit.get_current_price("KRW-BTC")
print(a)
# with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
#     lines = f.readlines()
#     access_key = lines[1].strip()
#     secret_key = lines[2].strip()
#     upbit = pyupbit.Upbit(access_key, secret_key)

# def buyable(aa):
#     price = aa
#     price = price * 1.002
#     if price - 1 < 0:
#         if price * 10 - 1 < 0:
#             price = price * 10000
#             price = math.floor(price)
#             price = price + 1
#             price = price / 10000
#         else:
#             price = price * 1000
#             price = math.floor(price)
#             price = price + 1
#             price = price / 1000
#     elif len(str(math.floor(price))) == 1:
#         price = price * 100
#         price = math.floor(price)
#         price = price + 1
#         price = price / 100
#     elif len(str(math.floor(price))) == 2:
#         price = price * 10
#         price = math.floor(price)
#         price = price + 1
#         price = price / 10
#     elif len(str(math.floor(price))) == 3:
#         price = math.floor(price)
#         price = price + 1
#     elif len(str(math.floor(price))) == 4:
#         if price % 10 <= 5: 
#             price = price / 10
#             price = math.floor(price)
#             price = price * 10
#             price = price + 5
#         else:
#             price = price / 10
#             price = math.floor(price)
#             price = price * 10
#             price = price + 10
#     elif len(str(math.floor(price))) == 5:
#         price = price / 10
#         price = math.floor(price)
#         price = price + 1
#         price = price * 10
#     elif len(str(math.floor(price))) == 6:
#         if (price/10) % 10 <= 5: 
#             price = price / 100
#             price = math.floor(price)
#             price = price * 100
#             price = price + 50
#         else:
#             price = price / 100
#             price = math.floor(price)
#             price = price * 100
#             price = price + 100
#     elif len(str(math.floor(price))) >=7:
#             price = price / 1000
#             price = math.floor(price)
#             price = price * 1000
#             price = price + 1000
#     return price

# print(buyable(249))