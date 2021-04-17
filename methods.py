# 方法库
from os import path, listdir, walk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo, askokcancel

import config


def try_find_device():
    """
    以导出播放列表为依据，检查是否存在设备
    存在：返回 所在盘符（*:\\)
    不存在：返回 False
    """
    for i in range(67, 91):
        driver_litter = chr(i)
        if path.isdir(driver_litter + ":\\" + config.Default.m0_folder):
            print("检查到已导出的播放列表文件夹，无需自定义路径.")
            print(("当前设备盘符为：" + driver_litter + ":\\"))
            m0_device = driver_litter + ":\\"
            return m0_device
    else:
        print("无法检索到设备，可能是从未导出过播放列表，请自行选取设备路径.")
        return False


def analysis_a_playlist(list_file_full_path):
    """
    解析一个列表，返回一个去除空行的列表
    list_file 为传入的列表全路径，类型为 str
    返回一个 list
    """
    with open(list_file_full_path, 'r', encoding='utf8') as file_object:
        tmp_list = file_object.readlines()
        # 去除所有的空行
        analysis_a_playlist_loop_inct = True
        while analysis_a_playlist_loop_inct:
            try:
                tmp_list.remove('\n')
            except ValueError:
                analysis_a_playlist_loop_inct = False
        return tmp_list


def get_all_files(floder_dir):
    """
    获取目录下所有文件
    floder_dir 是路径（包含斜杠）
    返回一个包含所有 文件全名 的列表
    """
    for root, dirs, files in walk(floder_dir):
        return files


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
        if not tmp:
            loop_inct = True
            print('未选择任何路径，将再次选择...')
            return 'Cancel'
        else:
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


def double_chk(title="二次确认", content="是否继续操作？"):
    """
    让用户决定是否继续操作
    :param title:提示框的标题
    :param content:提示框的内容
    :return: 继续:True  取消:False
    """
    tmp = askokcancel(title=title, message=content)
    return tmp
