from PyQt5 import QtWidgets
from GUI import Step11
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# 创建QApplication对象作GUI主程序入口
app = QApplication(sys.argv)


main = Step11.Ui_Step11()
rootW = QMainWindow()
main.setupUi(rootW)
rootW.show()
app.exec_()
