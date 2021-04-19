from PyQt5 import QtWidgets
import Step21, Step11
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
main = Step21.Ui_Step21()    # 创建主窗体对象，实例化Ui_MainWindow
rootW = QMainWindow()      # 实例化QMainWindow类
main.setupUi(rootW)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
rootW.show()
app.exec_()

main = Step11.Ui_Step11()    # 创建主窗体对象，实例化Ui_MainWindow
rootW = QMainWindow()      # 实例化QMainWindow类
main.setupUi(rootW)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
rootW.show()
app.exec_()
