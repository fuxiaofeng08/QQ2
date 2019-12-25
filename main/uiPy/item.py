# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from ..images import image_rc

class itemUI(object):
    def setupUi(self, data):
        self.frame = data['Form']
        self.frame.setGeometry(QtCore.QRect(150, 340, 266, 70))
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setStyleSheet("background: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        #设置控件名称为用户名称
        self.frame.setObjectName('frame')
        self.itemName = QtWidgets.QLabel(self.frame)
        self.itemName.setGeometry(QtCore.QRect(70, 10, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.itemName.setFont(font)
        self.itemName.setStyleSheet("color: rgb(59, 59, 59);background:none")
        self.itemName.setObjectName("itemName")
        self.itemgraph_10 = QtWidgets.QLabel(self.frame)
        self.itemgraph_10.setGeometry(QtCore.QRect(70, 32, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.itemgraph_10.setFont(font)
        self.itemgraph_10.setStyleSheet("color: rgb(144, 144, 144);background:none")
        self.itemgraph_10.setObjectName("itemgraph_10")
        self.itemPic = QtWidgets.QLabel(self.frame)
        self.itemPic.setGeometry(QtCore.QRect(10, 10, 50, 50))
        self.itemPic.setText("")
        self.itemPic.setPixmap(QtGui.QPixmap(data['pic']))
        self.itemPic.setScaledContents(True)
        self.itemPic.setObjectName("itemPic")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 266, 70))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setToolTip("")
        self.pushButton.setObjectName("pushButton")
        op = QtWidgets.QGraphicsOpacityEffect()
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0)
        self.pushButton.setGraphicsEffect(op)
        qssStyle = '''
                           QFrame:hover{background-color:lightgray}
                           QLabel:hover{background-color:lightgray}
                           '''
        self.frame.setStyleSheet(qssStyle)

        self.retranslateUi(data)
        self.pushButton.clicked.connect(partial(self.frame.DialogBox,data['usrName']))
        QtCore.QMetaObject.connectSlotsByName(self.frame)

    def retranslateUi(self, data):
        _translate = QtCore.QCoreApplication.translate
        self.itemName.setText(_translate("Form", data["usrName"]))
        self.itemgraph_10.setText(_translate("Form", data['autograph']))

