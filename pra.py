import math

def sellable(aa):
    price = aa
    # price = price * 0.998
    if price - 1 < 0:
        if price * 10 - 1 < 0:
            price = price * 10000
            price = math.floor(price)
            price = price - 1
            price = price / 10000
        else:
            price = price * 1000
            price = math.floor(price)
            price = price - 1
            price = price / 1000
    elif len(str(math.floor(price))) == 1:
        price = price * 100
        price = math.floor(price)
        price = price - 1
        price = price / 100
    elif len(str(math.floor(price))) == 2:
        price = price * 10
        price = math.floor(price)
        price = price / 10
    elif len(str(math.floor(price))) == 3:
        price = math.floor(price)
        price = price - 1
    elif len(str(math.floor(price))) == 4:
        if price % 10 <= 5: 
            price = price / 10
            price = math.floor(price)
            price = price * 10
        else:
            price = price / 10
            price = math.floor(price)
            price = price * 10
            price = price + 5
    elif len(str(math.floor(price))) == 5:
        price = price / 10
        price = math.floor(price)
        price = price * 10
    elif len(str(math.floor(price))) == 6:
        if (price/10) % 10 <= 5: 
            price = price / 100
            price = math.floor(price)
            price = price * 100
        else:
            price = price / 100
            price = math.floor(price)
            price = price * 100
            price = price + 50
    elif len(str(math.floor(price))) >=7:
        price = price / 1000
        price = math.floor(price)
        price = price * 1000
    return price

print(sellable(0.0133))