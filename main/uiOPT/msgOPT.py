import json
import time

from PyQt5.QtCore import QThread, pyqtSignal
from .. import setting



class sendThread(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            try:
                data = setting.SendMsgQ.get(timeout=0.1)
                setting.Client.sendMsg(data)
            except:
                pass

class recvThread(QThread):
    recvSingal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            recvMsg = setting.Client.recvMsg()
            self.recvSingal.emit(recvMsg)



