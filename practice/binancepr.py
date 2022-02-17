import ccxt
import datetime

with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    access_key = lines[2].strip()
    secret_key = lines[3].strip()
    binance = ccxt.binance({'apiKey': access_key, 'secret': secret_key})

btc_unit = binance.fetch_balance()["BTC"]['free']
if btc_unit > 0:
    print("hi")