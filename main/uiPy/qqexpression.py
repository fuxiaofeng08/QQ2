# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qqexpression.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QColor

from ..images import qqexpression_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setStyleSheet("background:none")
        self.Frame = Dialog
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("background:none")
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 200))
        self.scrollArea.setMaximumSize(QtCore.QSize(300, 200))
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 510))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.addItem()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def addItem(self):
        for i in range(132):
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.frame.setMinimumSize(QtCore.QSize(23, 23))
            self.frame.setMaximumSize(QtCore.QSize(23, 23))
            self.frame.resize(25,25)
            self.label = QtWidgets.QLabel(self.frame)
            self.label.setGeometry(QtCore.QRect(0, 0, 23, 23))
            picPath = ":/qqexpression/" + str(i + 1) + ".gif"
            self.gif = QMovie(picPath)
            self.label.setMovie(self.gif)
            self.label.setScaledContents(True)
            self.label.setMinimumSize(QtCore.QSize(23, 23))
            self.label.setMaximumSize(QtCore.QSize(23, 23))
            self.gif.start()
            self.label.setObjectName('l'+str(i))
            self.buttom = QtWidgets.QPushButton(self.frame)
            self.buttom.setGeometry(QtCore.QRect(0, 0, 23, 23))
            self.buttom.setMinimumSize(QtCore.QSize(23, 23))
            self.buttom.setMaximumSize(QtCore.QSize(23, 23))
            op = QtWidgets.QGraphicsOpacityEffect()
            # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
            op.setOpacity(0)
            self.buttom.setGraphicsEffect(op)
            self.buttom.setObjectName(str(i))
            self.frame.setStyleSheet('QFrame:hover{background-color:lightgray;}')
            self.buttom.setText(str(i))
            self.buttom.clicked.connect(partial(self.btnclk, str(i+1)))
            self.gridLayout.addWidget(self.frame, i //11, i % 11, 1, 1)
    def btnclk(self, data):
        self.Frame.hide()
        print(data)
        parent = self.Frame.parent()
        textEdit = parent.findChild(QtWidgets.QTextEdit, 'textEdit')
        tc = textEdit.textCursor()
        picPath = "D:/python_project/pycharmPro/QQ2/main/images/qqexpression/" + data + ".gif"
        tc.insertHtml("<img src=" + picPath + ">")


