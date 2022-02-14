import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pyupbit

tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-LTC"]
form_class = uic.loadUiType("bull.ui")[0]

class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def get_market_infos(self, ticker):
        df = pyupbit.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]
        price = pyupbit.get_current_price(ticker)

        state = None
        if price > last_ma5:
            state = "Bull"
        else:
            state = "Bear"

        return price, last_ma5, state

    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price, last_ma5, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(state)))


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec()
