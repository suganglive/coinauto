import pandas as pd

data = {"open":[737, 750, 770], "high":[755, 780, 770], "low":[700, 710, 750], "close":[750, 770, 730]}
index = ["2018-01-01", "2018-01-02", "2018-01-03"]
df = pd.DataFrame(data, index=index)
print(df)
a = df["high"] - df["low"]
df["volatility"] = a
print(df)


# url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
# df = pd.read_html(url)
# print(df[0]) 

# data = {"open": [100, 200], "high": [110, 210]}
# index = ['2021', '2022']
# df = DataFrame(data, index=index)
# print(df)

# date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
# xrp_close = [512, 512, 125, 325, 576]
# s = Series(xrp_close, index=date)
# print(s)