# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:\CodeS\M0_Playlist_Mgr\GUI\Step11.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Step11(object):
    def setupUi(self, Step11):
        Step11.setObjectName("Step11")
        Step11.setEnabled(True)
        Step11.resize(804, 381)
        Step11.setFocusPolicy(QtCore.Qt.ClickFocus)
        Step11.setAcceptDrops(True)
        Step11.setStyleSheet("background-color: rgb(255, 255, 255);")
        Step11.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.widget = QtWidgets.QWidget(Step11)
        self.widget.setObjectName("widget")
        self.label_text01 = QtWidgets.QLabel(self.widget)
        self.label_text01.setGeometry(QtCore.QRect(40, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_text01.setFont(font)
        self.label_text01.setMouseTracking(False)
        self.label_text01.setScaledContents(False)
        self.label_text01.setObjectName("label_text01")
        self.FolderPreview = QtWidgets.QListView(self.widget)
        self.FolderPreview.setGeometry(QtCore.QRect(220, 130, 291, 211))
        self.FolderPreview.setObjectName("FolderPreview")
        self.button_continue = QtWidgets.QPushButton(self.widget)
        self.button_continue.setGeometry(QtCore.QRect(520, 80, 241, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 134, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.button_continue.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.button_continue.setFont(font)
        self.button_continue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_continue.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_continue.setAutoFillBackground(False)
        self.button_continue.setStyleSheet("background-color: rgb(36, 134, 185);\n"
"color: rgb(255, 255, 255);")
        self.button_continue.setCheckable(False)
        self.button_continue.setDefault(True)
        self.button_continue.setFlat(False)
        self.button_continue.setObjectName("button_continue")
        self.button_exit = QtWidgets.QPushButton(self.widget)
        self.button_exit.setGeometry(QtCore.QRect(730, 30, 30, 30))
        self.button_exit.setStyleSheet("")
        self.button_exit.setObjectName("button_exit")
        self.button_minimize = QtWidgets.QPushButton(self.widget)
        self.button_minimize.setGeometry(QtCore.QRect(690, 30, 30, 30))
        self.button_minimize.setObjectName("button_minimize")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 80, 171, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_text02 = QtWidgets.QLabel(self.widget)
        self.label_text02.setGeometry(QtCore.QRect(220, 80, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_text02.setFont(font)
        self.label_text02.setMouseTracking(False)
        self.label_text02.setScaledContents(False)
        self.label_text02.setObjectName("label_text02")
        Step11.setCentralWidget(self.widget)

        self.retranslateUi(Step11)
        QtCore.QMetaObject.connectSlotsByName(Step11)

    def retranslateUi(self, Step11):
        _translate = QtCore.QCoreApplication.translate
        Step11.setWindowTitle(_translate("Step11", "M0 Playlist Mgr - Step 1"))
        self.label_text01.setText(_translate("Step11", "Select your device:"))
        self.button_continue.setText(_translate("Step11", "Continue"))
        self.button_exit.setText(_translate("Step11", "×"))
        self.button_minimize.setText(_translate("Step11", "_ "))
        self.radioButton.setText(_translate("Step11", "D:\\"))
        self.radioButton_2.setText(_translate("Step11", "E:\\"))
        self.label_text02.setText(_translate("Step11", "Device Preview:"))