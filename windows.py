# 窗口对象库
# ver.1

import PyQt5.QtWidgets
import sys


class MainWindow(PyQt5.QtWidgets.QApplication):
    def __init__(self, title):
        self.title = title
        super().__init__(self.title)

    def sw(self):
        app = PyQt5.QtWidgets.QApplication(sys.argv)
        # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
        w = PyQt5.QtWidgets.QWidget()
        # resize()方法调整窗口的大小。这离是250px宽150px高
        w.resize(250, 150)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        w.move(300, 300)
        # 设置窗口的标题
        w.setWindowTitle(self.title)
        # 显示在屏幕上
        w.show()


c = MainWindow('test')
