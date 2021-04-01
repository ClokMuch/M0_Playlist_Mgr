# 方法库
from os import path, listdir
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo

import config


def chk_if_device():
    """
    以导出播放列表检查是否存在设备
    存在：返回 所在盘符（*:\\)
    不存在：返回 False
    """
    for i in range(67, 91):
        driver_litter = chr(i)
        if path.isdir(driver_litter + ":\\" + config.Default.m0_folder):
            print("检查到已导出的播放列表文件夹，无需自定义路径.")
            m0_device = driver_litter + ":\\"
            return m0_device
    else:
        print("无法检索到设备，可能是从未导出过播放列表，请自行选取设备路径.")
        return False


def chk_if_playlist(driver_litter):
    """
    检查是否存在播放列表，以及是否为默认列表
    DriverLitter 为传入的驱动器，例如 C:\\

    仅存在 Default 列表 返回 'Default'
    仅存在非 Default 列表 返回 'Other'
    存在 Default 列表及其他列表 返回 True
    无列表或导出列表的文件夹 返回 False

    此函数主要为后期多列表可选择做准备
    '"""
    exist_default = 0
    exist_other = 0
    try:
        playlists = listdir(driver_litter + config.Default.m0_folder + "\\")
        if config.Default.playlist_default_name+config.Default.m0_playlist_type in playlists:
            exist_default = 1
        for i in playlists:
            if ".m3u" in i:
                if "Default.m3u" != i:
                    exist_other = 1
                    continue
        if exist_default == 1 and exist_other == 0:
            return 'Default'
        elif exist_default == 0 and exist_other == 1:
            return 'Other'
        elif exist_default == 1 and exist_other == 1:
            return True
        else:
            return False
    except FileNotFoundError:
        return False


def get_a_dir(is_dir=True):
    """
    选择一个路径，并返回以斜杠结尾的有效路径；
    对 is_dir 指定非 True 内容时，将再次选择，直到选择一个驱动器
    """
    loop_inct = True
    tmp = 0
    while loop_inct:
        tmp = askdirectory()
        if is_dir:
            tmp = tmp.replace("/", "\\") + '\\'
            loop_inct = False
        else:
            if tmp[-1] == '/':
                tmp = tmp.replace("/", "\\")
                loop_inct = False
            else:
                print("选择的对象不是一个驱动器的根目录，请选择驱动器的根目录（C:\\等）")
                showinfo(title="对象选择错误", message="请选择一个驱动器的根目录，如 C:\\ ，不要选择驱动器内的文件夹.")
    return tmp
