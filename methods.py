# 山灵M0播放器播放列表管理工具方法库
# ver.6
# By Clok Much

from os import path, listdir, walk
from tkinter.filedialog import askdirectory, askopenfilenames
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
            m0_device = driver_litter + ":\\"
            return m0_device
    else:
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
            showinfo(title="未选择驱动器", message="您取消选择，将重新自动检查设备路径.")
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


def get_musics():
    """
    返回包含完整路径的元组，以\\分割的路径
    若未选择文件，返回 0
    """
    original_musics = askopenfilenames()
    if original_musics:
        tmp = original_musics[:]
        for i in tmp:
            i.replace('/', '\\')
        return tmp
    else:
        print('没有选择任何文件.')
        return 0


def create_a_playlist(playlist_dir=None, playlist_name=None):
    """
    新建一个播放列表，必须传入播放列表完整路径以及播放列表的名称（不包含扩展名）
    扩展名由 config.py 配置
    :param playlist_dir: 播放列表路径（包含最后一个斜杠）
    :param playlist_name: 播放列表文件名（不包含扩展名）
    :return: 若文件已存在，返回：'Playlist_already_existed'
    若成功：返回 'Succeed'
    """
    # 检查路径下，文件是否重名，若重名返回 'Playlist_already_existed'
    floder_files = listdir(playlist_dir)
    full_playlist_name = playlist_name + config.Default.m0_playlist_type
    if full_playlist_name in floder_files:
        return 'Playlist_already_existed'

    # 创建播放列表
    with open(playlist_dir+full_playlist_name, 'w', encoding='utf8') as file_object:
        file_object.write('\n')
    return 'Succeed'


def select_a_playlist(dir_of_playlists):
    """
    选择一个播放列表
    :param list_of_playlists: 传入储存播放列表路径（不包含末尾斜杠）
    :return: 返回完整文件名
    """
    showinfo(title="发现多个列表", message="请在下一个界面选择需要处理的播放列表")
    playlist_full_path = askopenfilenames(title='选择一个播放列表文件',
                                          filetypes=[('Playlist file', config.Default.m0_playlist_type)],
                                          initialdir=dir_of_playlists)
    playlist_full_path = playlist_full_path[0]
    playlist_full_path.replace('/', '\\')
    return playlist_full_path


def output_a_playlist(list_of_musics, playlist_full_path):
    """
    将音乐列表储存为列表文件，编码为 utf8
    list_of_musics: 音乐列表
    playlist_full_path: 待处理播放列表完整路径与文件名
    :return: 直接处理文件，无返回值
    """
    with open(playlist_full_path, "w", encoding="utf8") as file_object:
        for i in list_of_musics:
            file_object.write(i)


def select_a_operation():
    """
    返回操作序列以选择操作
    :return: 操作序列，返回为int
        '1': '随机化',
        '2': '升序排序',
        '3': '重命名列表',
        '4': '退出程序'
    """
    operations = {
        '1': '随机化',
        '2': '升序排序',
        '3': '重命名列表（不删除当前列表）',
        '4': '退出程序'
    }
    selection_in = False
    while not selection_in:
        for key, value in operations.items():
            print(key + ':' + value)
        selection_in = input('请选择一个操作：')
        if selection_in not in operations.keys():
            selection_in = False
            print('输入无效，需要重新输入！\n')
    selection_in = int(selection_in)
    return selection_in
