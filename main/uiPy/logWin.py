# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ..images import image_rc

class Ui_LoadUI(object):
    def setupUi(self, LoadUI):
        LoadUI.setObjectName("LoadUI")
        LoadUI.setWindowModality(QtCore.Qt.NonModal)
        LoadUI.resize(530, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadUI.sizePolicy().hasHeightForWidth())
        LoadUI.setSizePolicy(sizePolicy)
        LoadUI.setMinimumSize(QtCore.QSize(0, 0))
        LoadUI.setMaximumSize(QtCore.QSize(530, 400))
        LoadUI.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        LoadUI.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/qq_reader.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        LoadUI.setWindowIcon(icon)
        self.topPic = QtWidgets.QLabel(LoadUI)
        self.topPic.setGeometry(QtCore.QRect(0, 0, 531, 151))
        self.topPic.setText("")
        self.topPic.setPixmap(QtGui.QPixmap(":/image/mainBackPic.png"))
        self.topPic.setObjectName("topPic")
        self.midPic = QtWidgets.QLabel(LoadUI)
        self.midPic.setGeometry(QtCore.QRect(215, 90, 100, 100))
        self.midPic.setStyleSheet("border-radius: 100;\n"
"border-color:\"red\";")
        self.midPic.setText("")
        self.midPic.setPixmap(QtGui.QPixmap(":/image/QQ2.png"))
        self.midPic.setScaledContents(True)
        self.midPic.setObjectName("midPic")
        self.usrName = QtWidgets.QLineEdit(LoadUI)
        self.usrName.setGeometry(QtCore.QRect(115, 200, 300, 35))
        self.usrName.setStyleSheet("padding-left:33;\n"
"border:none;")
        self.usrName.setInputMask("")
        self.usrName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usrName.setClearButtonEnabled(True)
        self.usrName.setObjectName("usrName")
        self.usrPwd = QtWidgets.QLineEdit(LoadUI)
        self.usrPwd.setGeometry(QtCore.QRect(115, 250, 300, 35))
        self.usrPwd.setStyleSheet("padding-left:33;\n"
"border:none;")
        self.usrPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usrPwd.setClearButtonEnabled(True)
        self.usrPwd.setObjectName("usrPwd")
        self.usrIcon = QtWidgets.QLabel(LoadUI)
        self.usrIcon.setGeometry(QtCore.QRect(120, 205, 25, 25))
        self.usrIcon.setText("")
        self.usrIcon.setPixmap(QtGui.QPixmap(":/image/unlog.png"))
        self.usrIcon.setScaledContents(True)
        self.usrIcon.setObjectName("usrIcon")
        self.pwdIcon = QtWidgets.QLabel(LoadUI)
        self.pwdIcon.setGeometry(QtCore.QRect(123, 257, 20, 20))
        self.pwdIcon.setText("")
        self.pwdIcon.setPixmap(QtGui.QPixmap(":/image/pwdIcon.png"))
        self.pwdIcon.setScaledContents(True)
        self.pwdIcon.setObjectName("pwdIcon")
        self.verticalFrame = QtWidgets.QFrame(LoadUI)
        self.verticalFrame.setGeometry(QtCore.QRect(115, 290, 300, 90))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remPwd = QtWidgets.QCheckBox(self.horizontalFrame)
        self.remPwd.setStyleSheet("color: rgb(135, 135, 135);")
        self.remPwd.setObjectName("remPwd")
        self.horizontalLayout.addWidget(self.remPwd)
        self.autoLog = QtWidgets.QCheckBox(self.horizontalFrame)
        self.autoLog.setMinimumSize(QtCore.QSize(0, 0))
        self.autoLog.setStyleSheet("color: rgb(135, 135, 135);")
        self.autoLog.setChecked(True)
        self.autoLog.setObjectName("autoLog")
        self.horizontalLayout.addWidget(self.autoLog)
        self.findPwd = QtWidgets.QPushButton(self.horizontalFrame)
        self.findPwd.setMinimumSize(QtCore.QSize(0, 0))
        self.findPwd.setStyleSheet("border:0;\n"
"background:none;\n"
"color: rgb(135, 135, 135);")
        self.findPwd.setObjectName("findPwd")
        self.horizontalLayout.addWidget(self.findPwd)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.loginBtn = QtWidgets.QPushButton(self.verticalFrame)
        self.loginBtn.setMinimumSize(QtCore.QSize(0, 45))
        self.loginBtn.setStyleSheet("background-color: rgb(17, 160, 255);\n"
"color:\"white\";\n"
"font-size:20px;\n"
"border-radius: 5px;\n"
"")
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout.addWidget(self.loginBtn)
        self.registerBtn = QtWidgets.QPushButton(LoadUI)
        self.registerBtn.setGeometry(QtCore.QRect(0, 360, 98, 35))
        self.registerBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.registerBtn.setStyleSheet("border:0;\n"
"background:none;\n"
"color: rgb(135, 135, 135);\n"
"")
        self.registerBtn.setObjectName("registerBtn")
        self.closeBtn = QtWidgets.QPushButton(LoadUI)
        self.closeBtn.setGeometry(QtCore.QRect(490, 10, 20, 20))
        self.closeBtn.setStyleSheet("border:0;\n"
"background:none;\n"
"")
        self.closeBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setObjectName("closeBtn")
        self.zoomIn = QtWidgets.QPushButton(LoadUI)
        self.zoomIn.setGeometry(QtCore.QRect(450, 10, 20, 20))
        self.zoomIn.setStyleSheet("border:0;\n"
"background:none;\n"
"")
        self.zoomIn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomIn.setIcon(icon2)
        self.zoomIn.setFlat(False)
        self.zoomIn.setObjectName("zoomIn")

        self.retranslateUi(LoadUI)
        self.closeBtn.clicked.connect(LoadUI.close)
        self.zoomIn.clicked.connect(LoadUI.showMinimized)
        self.usrName.textEdited['QString'].connect(LoadUI.inputName)
        self.usrPwd.textEdited['QString'].connect(LoadUI.inputPwd)
        self.loginBtn.clicked.connect(LoadUI.loginBtn)
        self.registerBtn.clicked.connect(LoadUI.register)
        QtCore.QMetaObject.connectSlotsByName(LoadUI)

    def retranslateUi(self, LoadUI):
        _translate = QtCore.QCoreApplication.translate
        self.usrName.setPlaceholderText(_translate("LoadUI", "QQ号码/手机号/邮箱"))
        self.usrPwd.setPlaceholderText(_translate("LoadUI", "密码"))
        self.remPwd.setText(_translate("LoadUI", "记住密码"))
        self.autoLog.setText(_translate("LoadUI", "自动登录"))
        self.findPwd.setText(_translate("LoadUI", "找回密码"))
        self.loginBtn.setText(_translate("LoadUI", "登  录"))
        self.registerBtn.setText(_translate("LoadUI", "注册账号"))

