import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QTextBrowser, QTextEdit

from main.uiPy import qqexpression
from main.ui.temp import Ui_Dialog as ui

class myWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    def sendText(self):
        Browser = self.findChild(QTextBrowser, 'textBrowser')
        edit = self.findChild(QTextEdit, 'textEdit')
        print(Browser, edit)
        text = edit.toHtml()
        Browser.append(text)

    def sendExpress(self):
        expressUI = QtWidgets.QFrame(self)
        expressUI.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ui = qqexpression.Ui_Dialog()
        ui.setupUi(expressUI)
        expressUI.show()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = myWin()
    ui = ui()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())


