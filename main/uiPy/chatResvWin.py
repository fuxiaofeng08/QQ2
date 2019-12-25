# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatResvWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ..images import image_rc


class chatResvItem(object):
    def setupUi(self, data):
        self.frame = data['Dialog']
        self.frame.setGeometry(QtCore.QRect(100, 90, 706, 52))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.friendpic = QtWidgets.QLabel(self.frame)
        self.friendpic.setMinimumSize(QtCore.QSize(30, 30))
        self.friendpic.setMaximumSize(QtCore.QSize(30, 30))
        self.friendpic.setText("")
        self.friendpic.setTextFormat(QtCore.Qt.AutoText)
        self.friendpic.setPixmap(QtGui.QPixmap(":/image/QQ4.jpg"))
        self.friendpic.setScaledContents(True)
        self.friendpic.setObjectName("friendpic")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.friendpic)
        self.fchatwin = QtWidgets.QLabel(self.frame)
        self.fchatwin.setMinimumSize(QtCore.QSize(0, 18))
        self.fchatwin.setStyleSheet("border-bottom:1px solid lightgray;")
        self.fchatwin.setScaledContents(True)
        self.fchatwin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fchatwin.setWordWrap(True)
        self.fchatwin.setObjectName("fchatwin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fchatwin)

        self.retranslateUi(data)
        QtCore.QMetaObject.connectSlotsByName(self.frame)

    def retranslateUi(self, data):
        _translate = QtCore.QCoreApplication.translate
        self.fchatwin.setText(_translate("Dialog", data['msg']))

