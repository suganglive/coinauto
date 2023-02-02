import requests
from bs4 import BeautifulSoup

url = 'https://upbit.com/exchange?code=CRIX.UPBIT.KRW-NU'

res = requests.get(url)
print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

