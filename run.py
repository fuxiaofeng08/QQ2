import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from main.uiPy.logWin import Ui_LoadUI
from main.uiOPT.Signin import MyWindow
from main.Conn.conn import client
from main import setting
from main.uiOPT import msgOPT
from main import setting
from main.uiOPT import dataDisrti

def LoadUI():
    mainUI = MyWindow()
    mainUI.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = Ui_LoadUI()
    ui.setupUi(mainUI)
    return mainUI
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainUI = LoadUI()
    setting.WinDict["loadInfo"] = mainUI
    mainUI.show()
    setting.Client = client()
    try:
        setting.Client.run()
        t1 = msgOPT.sendThread()
        t2 = msgOPT.recvThread()
        t2.recvSingal.connect(dataDisrti.dataDistri)
        t1.start()
        t2.start()
        setting.ConnStat = True
    except:
        QMessageBox.about(mainUI,'网络提示', "主界面网络连接错误")


    sys.exit(app.exec_())
