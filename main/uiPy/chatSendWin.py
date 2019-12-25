# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatUsrWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ..images import image_rc

class chatSendItem(object):
    def __init__(self):
        print(">chatroom发送消息配置")
    def setupUi(self, data):
        self.currentUsr = data['Dialog']
        self.currentUsr.setGeometry(QtCore.QRect(80, 60, 706, 114))
        self.currentUsr.setMinimumSize(QtCore.QSize(0, 40))
        self.currentUsr.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.currentUsr.setStyleSheet("")
        self.currentUsr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currentUsr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentUsr.setObjectName("currentUsr")
        self.formLayout_2 = QtWidgets.QFormLayout(self.currentUsr)
        self.formLayout_2.setObjectName("formLayout_2")
        self.usrpic = QtWidgets.QLabel(self.currentUsr)
        self.usrpic.setMinimumSize(QtCore.QSize(30, 30))
        self.usrpic.setMaximumSize(QtCore.QSize(30, 30))
        self.usrpic.setText("")
        self.usrpic.setPixmap(QtGui.QPixmap(":/image/QQ (8).png"))
        self.usrpic.setScaledContents(True)
        self.usrpic.setObjectName("usrpic")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usrpic)
        self.usrchatwin = QtWidgets.QLabel(self.currentUsr)
        self.usrchatwin.setMinimumSize(QtCore.QSize(0, 18))
        self.usrchatwin.setStyleSheet("border-bottom:1px solid lightgray;")
        self.usrchatwin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.usrchatwin.setObjectName("usrchatwin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usrchatwin)
        self.retranslateUi(data)
        QtCore.QMetaObject.connectSlotsByName(self.currentUsr)

    def retranslateUi(self, data):
        _translate = QtCore.QCoreApplication.translate
        self.usrchatwin.setText(_translate("Dialog", data['msg']))

