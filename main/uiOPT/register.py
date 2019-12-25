import json

from PyQt5.Qt import *
from PyQt5 import QtWidgets, QtCore
import requests
from .. import setting
class RegWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.pwd1 = ''
        self.pwd2 = ''
        self.flag = False
    #1.鼠标点击事件
    def mousePressEvent(self,evt):
        # 获取鼠标当前的坐标
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()
        # 获取窗体当前坐标
        self.origin_x = self.x()
        self.origin_y = self.y()
    #2.鼠标移动事件
    def mouseMoveEvent(self,evt):
        # 计算鼠标移动的x，y位移
        move_x = evt.globalX() - self.mouse_x
        move_y = evt.globalY() - self.mouse_y
        # 计算窗体更新后的坐标：更新后的坐标 = 原本的坐标 + 鼠标的位移
        dest_x = self.origin_x + move_x
        dest_y = self.origin_y + move_y
        # 移动窗体
        self.move(dest_x,dest_y)
    def getName(self):
        usrName = self.sender().text()
        self.name = usrName
    def firstPwd(self):
        print("firstPwd",self.sender().text())
        self.pwd1 = self.sender().text()
    def secondPwd(self):
        print("secondPwd",self.sender().text())
        self.pwd2 = self.sender().text()
    def accept(self):
        Client = setting.Client
        # 判断连接状态是不是正常
        if not setting.ConnStat:
            try:
                Client.run()
            except:
                print("服务器连接失败")
                QtWidgets.QMessageBox.about(self, '网络提示', "服务器连接失败")
                return
        if self.pwd1 == self.pwd2:
            radioman = self.findChild(QRadioButton, 'radioman')
            if radioman.isChecked():
                sex = 'man'
            else:
                sex = 'women'
            data = {
                'usrName':self.name,
                'pwd':self.pwd1,
                'sex':sex
            }
            sendmsg = {
                'Register':data
            }
            setting.SendMsgQ.put(json.dumps(sendmsg))
        else:
            QtWidgets.QMessageBox.about(self, '登录提示', '密码不一致    ')
    def reject(self):
        from run import LoadUI
        self.hide()
        self.win = LoadUI()
        self.win.show()

    def recvMsg(self, data):
        if data['Register'] == 'Exist':
            QtWidgets.QMessageBox.about(self, '注册提示', '用户已存在  ')
        if data['Register'] == 'OK':
            QtWidgets.QMessageBox.about(self, '注册提示', '注册成功  ')
            self.close()
            setting.WinDict['loadInfo'].show()
        else:
            QtWidgets.QMessageBox.about(self, '注册提示', '注册失败  ')
