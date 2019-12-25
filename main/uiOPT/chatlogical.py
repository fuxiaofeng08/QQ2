import json
from PyQt5 import QtCore, QtWidgets
from ..uiPy.chatSendWin import chatSendItem
from ..uiPy.chatResvWin import chatResvItem
from ..images import image_rc
from .. import setting
from ..uiPy import qqexpression

###################消息格式说明#####################
#   msg = {‘flag’:msg}
#   flag == LoadInfo 表示本次请求为登录请求
#   flag == LoadFriends 表示本次请求为获取好友列表请求
#   flag == {Friend} 表示发送消息至Friend
#################################################

class chatRoom(QtWidgets.QDialog):
    def __init__(self, usrName):
        super().__init__()
        self.setWindowTitle(usrName)
        self.usrName = usrName
        print(usrName,">聊天窗口初始化<")
    #获取用户输入消息，创建显示信息单元
    def sendmsg(self):
        textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        sendMsg = textEdit.toPlainText()#获取用户输入
        print("用户输入信息", sendMsg)
        chatscrollArea = self.findChild(QtWidgets.QWidget, 'chatscrollArea')#获取chatscrollArea控件
        chatFrame = QtWidgets.QFrame(chatscrollArea)#在chascrollArea控件上创建对话框控件
        data = {
            'Dialog':chatFrame,
            'msg':sendMsg
        }
        msg = {
            self.usrName:sendMsg
        }
        setting.SendMsgQ.put(json.dumps(msg))
        win = chatSendItem()
        win.setupUi(data)
        self.addToScroll(chatFrame)

    def recvMsg(self, recv):#接受用户消息
        for key in recv:
            recvmsg = recv[key]
        chatscrollArea = self.findChild(QtWidgets.QWidget, 'chatscrollArea')  # 获取chatscrollArea控件
        chatFrame = QtWidgets.QFrame(chatscrollArea)  # 在chascrollArea控件上创建对话框控件
        data = {
            'Dialog': chatFrame,
            'msg': recvmsg
        }
        win = chatResvItem()
        win.setupUi(data)
        self.addToScroll(chatFrame)
    #追加信息单元至显示界面最后
    def addToScroll(self,item):
        verticalLayout = self.findChild(QtWidgets.QVBoxLayout, 'verticalLayout_6')
        verticalLayout.insertWidget(verticalLayout.count() - 1, item)
        chatscrollArea = self.findChild(QtWidgets.QScrollArea, 'chatwin')
        self.scrollBar = chatscrollArea.verticalScrollBar()
        self.scrollBar.setValue(verticalLayout.count() * 40)

    def choseExpress(self):
        expressUI = QtWidgets.QFrame(self)
        expressUI.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ui = qqexpression.Ui_Dialog()
        ui.setupUi(expressUI)
        expressUI.move(0, self.height() - 385)
        expressUI.show()






