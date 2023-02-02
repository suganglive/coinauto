from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/sugang/Documents/GitHub/coinauto/chromedriver')
# driver.get("https://upbit.com/exchange?code=CRIX.UPBIT.KRW-WAVES")
driver.get("https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC")
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
ans = soup.find("a", {"class": "tag tooltipDown"})
if ans:
    print('hi')
    print(ans)
else:
    print('no')
    print(ans)