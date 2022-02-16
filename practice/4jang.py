import requests
from bs4 import BeautifulSoup
import datetime

url = "https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw"
r = requests.get(url)
bitcoin = r.json()

timestamp = bitcoin['timestamp']
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)

# url = "https://finance.naver.com/item/main.nhn?code=000660"
# res = requests.get(url)

# soup = BeautifulSoup(res.text, "html.parser")
# tags = soup.find("table", {"class":"lwidth"}).find("tr", {"class":"strong"})
# print(tags.em.text[:-1])


# def get_per(code):
#     url = "https://finance.naver.com/item/main.nhn?code=" + code
#     res = requests.get(url)

#     soup = BeautifulSoup(res.text, "html.parser")
#     tags = soup.select("#_per")
#     tag = tags[0]
#     return float(tag.text)

# def get_dividend(code):
#     url = "https://finance.naver.com/item/main.nhn?code=" + code
#     res = requests.get(url)

#     soup = BeautifulSoup(res.text, "html.parser")
#     tags = soup.select("#_dvr")
#     tag = tags[0]
#     return float(tag.text)

# print(get_per("000660"))
# print(get_dividend("000660"))

