# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'K:\CodeS\M0_Playlist_Mgr\GUI\Step10.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Step10(object):
    def setupUi(self, Step10):
        Step10.setObjectName("Step10")
        Step10.resize(804, 381)
        Step10.setFocusPolicy(QtCore.Qt.ClickFocus)
        Step10.setAcceptDrops(True)
        Step10.setStyleSheet("background-color: rgb(255, 255, 255);")
        Step10.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.widget = QtWidgets.QWidget(Step10)
        self.widget.setObjectName("widget")
        self.label_text01 = QtWidgets.QLabel(self.widget)
        self.label_text01.setGeometry(QtCore.QRect(110, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_text01.setFont(font)
        self.label_text01.setMouseTracking(False)
        self.label_text01.setScaledContents(False)
        self.label_text01.setObjectName("label_text01")
        self.label_device = QtWidgets.QLabel(self.widget)
        self.label_device.setGeometry(QtCore.QRect(50, 30, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_device.setFont(font)
        self.label_device.setMouseTracking(False)
        self.label_device.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_device.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_device.setScaledContents(False)
        self.label_device.setObjectName("label_device")
        self.FolderPreview = QtWidgets.QListView(self.widget)
        self.FolderPreview.setGeometry(QtCore.QRect(50, 130, 411, 211))
        self.FolderPreview.setObjectName("FolderPreview")
        self.label_capacity = QtWidgets.QLabel(self.widget)
        self.label_capacity.setGeometry(QtCore.QRect(50, 80, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_capacity.setFont(font)
        self.label_capacity.setMouseTracking(False)
        self.label_capacity.setScaledContents(False)
        self.label_capacity.setObjectName("label_capacity")
        self.button_yes = QtWidgets.QPushButton(self.widget)
        self.button_yes.setGeometry(QtCore.QRect(520, 130, 241, 91))
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
        self.button_yes.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.button_yes.setFont(font)
        self.button_yes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_yes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_yes.setAutoFillBackground(False)
        self.button_yes.setStyleSheet("background-color: rgb(36, 134, 185);\n"
"color: rgb(255, 255, 255);")
        self.button_yes.setCheckable(False)
        self.button_yes.setDefault(True)
        self.button_yes.setFlat(False)
        self.button_yes.setObjectName("button_yes")
        self.button_exit = QtWidgets.QPushButton(self.widget)
        self.button_exit.setGeometry(QtCore.QRect(730, 30, 30, 30))
        self.button_exit.setStyleSheet("")
        self.button_exit.setObjectName("button_exit")
        self.button_minimize = QtWidgets.QPushButton(self.widget)
        self.button_minimize.setGeometry(QtCore.QRect(690, 30, 30, 30))
        self.button_minimize.setObjectName("button_minimize")
        self.button_no = QtWidgets.QPushButton(self.widget)
        self.button_no.setGeometry(QtCore.QRect(520, 250, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.button_no.setFont(font)
        self.button_no.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_no.setStyleSheet("background-color: rgb(135, 61, 36);\n"
"color: rgb(255, 255, 255);")
        self.button_no.setObjectName("button_no")
        Step10.setCentralWidget(self.widget)

        self.retranslateUi(Step10)
        QtCore.QMetaObject.connectSlotsByName(Step10)

    def retranslateUi(self, Step10):
        _translate = QtCore.QCoreApplication.translate
        Step10.setWindowTitle(_translate("Step10", "M0 Playlist Mgr - Step 1"))
        self.label_text01.setText(_translate("Step10", "is your device?"))
        self.label_device.setText(_translate("Step10", ))
        self.label_capacity.setText(_translate("Step10", "Capacity: Used/All"))
        self.button_yes.setText(_translate("Step10", "Yes,\n"
"this is my device."))
        self.button_exit.setText(_translate("Step10", "×"))
        self.button_minimize.setText(_translate("Step10", "_ "))
        self.button_no.setText(_translate("Step10", "No,\n"
"this is NOT my device."))