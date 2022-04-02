from pybithumb import WebSocketManager

class Worker():
    def run(self):
        wm = WebSocketManager("ticker", ["BTC_KRW"])
        while True:
            data = wm.get()
            self.recv.emit(data['content']['closePrice'])
            print(data)

