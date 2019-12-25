import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSlot, QStringListModel
import sys
from ..uiPy.mainWin import Ui_Form
from ..uiPy.item import itemUI
from .. import setting
import json
#切换至聊天框
class DialogBox(QtWidgets.QFrame):
    def DialogBox(self, usrName):
        print("recv", usrName)
        from ..uiPy.chatWin import Ui_Dialog
        from ..uiOPT.chatlogical import chatRoom
        ui = Ui_Dialog()
        self.win = chatRoom(usrName)
        setting.WinDict[usrName] = self.win
        ui.setupUi(self.win)
        self.win.setObjectName(usrName)
        self.win.show()


class mainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.clt = setting.Client
        self.ShName = '' #记录需要搜索的信息

#窗口移动
    def mousePressEvent(self, evt):
        # 获取鼠标当前的坐标
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()
        # 获取窗体当前坐标
        self.origin_x = self.x()
        self.origin_y = self.y()
        # 2.鼠标移动事件
    def mouseMoveEvent(self, evt):
        # 计算鼠标移动的x，y位移
        move_x = evt.globalX() - self.mouse_x
        move_y = evt.globalY() - self.mouse_y
        # 计算窗体更新后的坐标：更新后的坐标 = 原本的坐标 + 鼠标的位移
        dest_x = self.origin_x + move_x
        dest_y = self.origin_y + move_y
        # 移动窗体
        self.move(dest_x, dest_y)
#登录成功获取好友列表并刷新
    def sendFReQ(self):
        info = {
                'LoadFriends':'friends'
        }
        #向服务器发送获取好友列表的验证消息
        setting.SendMsgQ.put(json.dumps(info))
    #接受好友列表并添加
    def recvMsg(self,resp):
        self.formLastConn = self.findChild(QWidget, 'scrollAreaWidgetContents')
        friends = resp['friends']
        friends = json.loads(friends)
        def sortF(f):
            return f['state']
        friends.sort(key=sortF)
        # 好友列表
        for item in friends:
            items = itemUI()
            form = DialogBox(self.formLastConn)
            usrName = item['usrName']
            autograph = item['autograph']
            if item['state']:
                picPath = ":/image/QQ2.png"
            else:
                picPath = ":/image/unlog.png"
            data = {
                'Form': form,
                'usrName': usrName,
                'autograph': autograph,
                'pic':picPath
            }
            items.setupUi(data)
            form.setObjectName(usrName + 'item')
            self.vLayoutLastConn = self.findChild(QVBoxLayout, 'verticalLayout_4')
            self.vLayoutLastConn.insertWidget(self.vLayoutLastConn.count() - 1, form)
    #获取需要添加的好友
    def searchUsr(self):
        self.ShName= self.sender().text()

    # 发送需要添加用户关键字
    def search(self):
        searchData = {
            'searchFriend':self.ShName
        }
        data = json.dumps(searchData)
        setting.SendMsgQ.put(data)
    #显示存在该关键字的相关用户
    def displaySearchRst(self,data):
        self.usrLst = data['searchFriend']
        listView = self.findChild(QListView, 'listView')
        listModel = QStringListModel()
        listModel.setStringList(self.usrLst)
        listView.setModel(listModel)
        listView.clicked.connect(self.checkItem)
    #获取选择的需要添加的好友
    def checkItem(self,index):
        self.friendReq = self.usrLst[index.row()]
        labelView = self.findChild(QLabel, 'selectUsr')
        labelView.setText(self.friendReq)
    #发送添加好友的信息
    def add(self):
        usrName = self.friendReq
        sendMsg = {
            'addFriend':usrName
        }
        setting.SendMsgQ.put(json.dumps(sendMsg))
    #获取添加好友信息的回复
    def addResp(self,data):
        print(data)
        if 'YES' in data['addFriend']:
            QMessageBox.about(self, '添加好友消息', '添加好友%s成功'%self.friendReq)
        elif 'NO' in data['addFriend']:
            QMessageBox.about(self, '添加好友消息', '%s拒绝了你的好友申请' % self.friendReq)
        else:
            reply = QMessageBox.question(self,'申请好友', '%s请求添加你为好友'%data['addFriend'],QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if str(reply) == '16384':
                resp = 'YES'
            else:
                resp = 'NO'
            respData = {
                'addFriend':resp + data['addFriend']
            }
            setting.SendMsgQ.put(json.dumps(respData))















