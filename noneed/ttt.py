import time
import datetime

now = datetime.datetime.now()
nine = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours=7, minutes=10)
if now > nine:
    nine = nine + datetime.timedelta(1)

while True:
    now = datetime.datetime.now()
    if nine < now < nine + datetime.timedelta(seconds=10):
        nine = nine = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days= 1, hours=7, minutes=10)
        print("hi")
        print(nine)
    else:
        print("yet")
    time.sleep(1)