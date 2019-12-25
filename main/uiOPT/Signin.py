import time

from PyQt5.Qt import *
from PyQt5 import QtWidgets, QtCore
from .. import setting
import json

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        print("登录模块启动")
        self.name = ''
        self.pwd = ''
        self.usrInfo = ''
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
    def inputName(self, name):
        self.name = name
    def inputPwd(self, pwd):
        self.pwd = pwd
    #用户登录
    def loginBtn(self):
        Client = setting.Client
        #判断连接状态是不是正常
        if not setting.ConnStat:
            try:
                Client.run()
            except:
                print("服务器连接失败")
                QtWidgets.QMessageBox.about(self,'网络提示', "服务器连接失败")
                return
        if self.pwd == '' or self.name == '':
            QtWidgets.QMessageBox.about(self,'登录提示', "用户名和密码不能为空")
            return
        data = {
            'usrName':self.name,
            'pwd':self.pwd
        }
        data = json.dumps(data)
        msg = {'LoadInfo':data}
        msg = json.dumps(msg)
        setting.SendMsgQ.put(msg)
    def recvMsg(self, data):
        resp = data
        if resp["loadInfo"] != 'NO':
            # 创建主窗口显示
            from ..uiPy.mainWin import Ui_Form
            from ..uiOPT.mainlogical import mainWin
            print('sssss')
            self.close()
            self.mainWin = mainWin()
            # 添加窗口到字典保存
            setting.WinDict['friends'] = self.mainWin
            self.mainWin.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.usrInfo = json.loads(resp['loadInfo'])
            autograph = self.usrInfo['autograph']
            ui = Ui_Form()
            ui.setupUi(self.mainWin)
            # 设置主窗口信息
            picQ = self.mainWin.findChild(QLabel, 'usrPic')
            # 主窗口显示用户名和个人签名
            nameQ = self.mainWin.findChild(QLabel, 'Name')
            autographQ = self.mainWin.findChild(QLabel, 'autoGraph')
            nameQ.setText(self.name)
            autographQ.setText(autograph)
            desktop = QtWidgets.QApplication.desktop()
            move_x = desktop.width() - 400
            move_y = 50
            self.mainWin.move(move_x, move_y)
            self.mainWin.show()
            # 获取好友列表请求
            self.mainWin.sendFReQ()
        else:
            QMessageBox.about(self, '登录提示', '用户名或密码错误')
            return

    #用户注册
    def register(self):
        from ..uiPy.regWin import Ui_regUI
        from ..uiOPT.register import RegWindow
        self.hide()
        self.win = RegWindow()
        self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ui = Ui_regUI()
        ui.setupUi(self.win)
        setting.WinDict['Register'] = self.win
        self.win.show()
        print(">>>用户注册界面调用")




