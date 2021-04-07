# M0_Playlist_Mgr GUI.ver
# By Clok Much
# ver.1

import methods
from GUI import GUI

# step0.0:检查是否存在 M0 播放列表
if methods.chk_if_device():
    if methods.chk_if_playlist(methods.chk_if_device()):
        GUI.Ui_Step10
        import sys
        # 创建一个QApplication，也就是你要开发的软件app
        MainWindow = GUI.QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
        ui = GUI.Ui_Step10  # ui是你创建的ui类的实例化对象
        ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
        MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
        #sys.exit()  # 使用exit()或者点击关闭按钮退出QApplication