import ccxt
import datetime
from binance.client import Client

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[2].strip()
    secret_key = lines[3].strip()
    binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[2].strip()
    secret_key = lines[3].strip()
    client = Client(access_key, secret_key)

# btc_unit = binance.fetch_balance()["BTC"]['free']
# if btc_unit > 0:
#     print("hi")

# print(binance.fetch_balance()["BTC"]["total"])

binance.create_limit_buy_order("ETH/USDT", 0.005136124238423859237589247298579284579284123123, 2901)


