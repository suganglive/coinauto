from pyupbit import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import websockets
# import asyncio
# import json

# async def upbit_ws_client():
#     uri = "wss://api.upbit.com/websocket/v1"

#     async with websockets.connect(uri, ping_interval=60) as websocket:
#         subscribe_fmt = [{"ticket":"test"}, {"type":"ticker", "codes":["KRW-BTC"], "isOnlyRealtime":True}, {"format":"SIMPLE"}]
#         subscribe_data = json.dumps(subscribe_fmt)
#         await websocket.send(subscribe_data)

#         while True:
#             data = await websocket.recv()
#             data = json.loads(data)
#             print(data)
        
# async def main():
#     await upbit_ws_client()

# asyncio.run(main())
class Worker(QThread):
    recv = pyqtSignal(dict)

    def run(self):
        #create websocke for upbit
        wm = WebSocketManager("ticker", ["KRW-BTC"])
        while True:
            data = wm.get()
            print(data)
            self.recv.emit(data)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__

        label = QLabel("BTC", self)
        label.move(20,20)

        self.price = QLabel("", self)
        self.price.move(80, 20)
        self.price.resize(100,20)

        button = QPushButton("Start", self)
        button.move(20, 50)
        button.clicked.connect(self.click_btn)

        self.th = Worker()
        self.th.recv.connect(self.receive_msg)

    @pyqtSlot(dict)
    def receive_msg(self, data):
        print(data)
        close_price = data.get("trade_price")
        self.price.setText(str(close_price))
    
    def click_btn(self):
        self.th.start()

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()