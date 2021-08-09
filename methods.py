# 山灵M0播放器播放列表管理工具通用方法库
# ver.11
# By Clok Much

from os import path, listdir, walk

from tkinter.filedialog import askdirectory, askopenfilenames
from tkinter.messagebox import showinfo, askokcancel

import config


def try_find_device():
    """
    以导出播放列表为依据，检查是否存在设备
    存在：返回 所在盘符（*:\\)：若仅有一个，返回为 str ；若有多个，返回为 list .
    不存在：返回 False
    """
    devices_list = []
    for i in range(67, 91):
        driver_litter = chr(i)
        if path.isdir(driver_litter + ":\\" + config.Default.m0_folder):
            m0_device = driver_litter + ":\\"
            devices_list.append(m0_device)
    if len(devices_list) == 1:
        return devices_list[0]
    elif not devices_list:
        return False
    else:
        return devices_list


def explore_devices():
    """
    以导出播放列表为依据，检查是否存在设备
    :return: 对应设备盘符的列表，不存在时返回空列表  ['F:\\', 'G:\\']
    """
    result = []
    for i in range(67, 91):
        driver_litter = chr(i) + ":\\"
        if path.isdir(driver_litter + config.Default.m0_folder):
            result.append(driver_litter)
    return result


def analysis_playlist(list_file_full_path):
    """
    解析一个列表
    list_file 为传入的列表全路径，类型为 list
    返回一个 dict {列表全路径: [去除空行的内容列表]}
    """
    result = {}
    for i in list_file_full_path:
        result[i] = 'Default\n'  # 为字典创建键值对
    for i in result.keys():
        with open(i, 'r', encoding='utf8') as file_object:
            result[i] = file_object.readlines()
            # 去除所有的空行
            while True:
                try:
                    result[i].remove('\n')
                except ValueError:
                    break
    return result


def get_all_files(floder_dir):
    """
    获取目录下所有文件
    floder_dir 是路径（包含斜杠）
    返回一个包含所有 文件全名 的列表
    """
    for root, dirs, files in walk(floder_dir):
        return files


def get_a_dir(is_dir=True, tips='Select a location...'):
    """
    选择一个路径，并返回以斜杠结尾的有效路径；
    ▲ 这里有一个坑：获取目录的含树没有想到指定为我的电脑初始路径的方法
    """
    while True:
        result = askdirectory(title=tips)
        if not result:
            print("未选择任何内容.")
            showinfo(title="您必须选择一个！", message="您必须选择一个内容，请在下一个窗体中选择...")
            continue
        else:
            result = result.replace("/", "\\") + "\\"
        if is_dir:  # 要求选择路径
            return result
        else:   # 要求选择驱动器
            result = result[:3]
            return result


def double_chk(title="二次确认", content="是否继续操作？"):
    """
    让用户决定是否继续操作
    :param title:提示框的标题
    :param content:提示框的内容
    :return: 继续:True  取消:False
    """
    tmp = askokcancel(title=title, message=content)
    return tmp


'''
此函数已废弃
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
'''


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
    with open(playlist_dir + full_playlist_name, 'w', encoding='utf8') as file_object:
        file_object.write('\n')
    return 'Succeed'


def select_playlist(dir_of_playlists):
    """
    选择一个或多个播放列表
    list_of_playlists: 传入储存播放列表路径（包含末尾斜杠）
    :return: 返回含有完整文件名的列表
    """
    playlist_full_path = None
    while not playlist_full_path:
        showinfo(title="发现多个列表",
                 message="请在下一个界面选择需要处理的播放列表.\n\n"
                         "默认只显示已启用的列表，如果需要选择禁用的列表，请在右下文件类型处切换选择.")
        playlist_full_path = askopenfilenames(title='选择一个或多个播放列表文件',
                                              filetypes=[
                                                  ('Playlist file', config.Default.m0_playlist_type),
                                                  ('Disabled playlist file', config.Default.m0_disabled_playlist),
                                                  ('All files', '*')
                                              ],
                                              initialdir=dir_of_playlists)
        if not playlist_full_path:
            showinfo(title="未选择任何一个播放列表",
                     message="您未选择任何一个播放列表，您需要选择一个播放列表才可以继续.\n\n"
                             "默认只显示已启用的列表，如果需要选择禁用的列表，请在右下文件类型处切换选择.")
    playlist_full_path = list(playlist_full_path)
    result = []
    for i in playlist_full_path:
        result.append(i.replace('/', '\\'))
    return result


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


'''
此函数已废弃
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
'''


def universal_selections(tips='', selections=None):
    """
    获取输入选项并判断是否合理，无误后返回选择结果
    tips: 字符串，列出选项前的提示语
    selections: 字典，输入的选择条目 {'序号': ('提示/说明', '内部指令')}
    :return: string，输出的选择结果
    """
    if type(selections) != dict:
        print("##内部错误：def universal_selections 传入的 selections 不是 dict 类型！")
    if tips:
        print(tips)
    for key, value in selections.items():
        print(key + ':' + value[0])
    while True:
        result = input('请选择一个操作：')
        if result not in selections.keys():
            print('输入无效，需要重新输入！')
            continue
        else:
            result = selections[result][1]
            return result


def universal_analysis(target):
    """
    分析一个文件，返回易于处理的格式，自动去除空行，仅适用于一个文件
    :param target: str 待分析的文件完整位置
    :return: [target_path, [content_list]]
    """
    if type(target) != str:
        print('#InnerError:methods.universal_analysis: target is not str.')
        return '#InnerError:methods.universal_analysis: target is not str.'
    else:
        result = [target, []]
        try:
            with open(target, 'r', encoding='utf8') as file_object:
                tmp = file_object.readlines()   # 去除空行
                for i in tmp:
                    if i == '\n':
                        continue
                    else:
                        result[1].append(i)
                return result
        except IOError:
            print('#InnerError:methods.universal_analysis: target is not exist or readable/IOError.')
            return '#InnerError:methods.universal_analysis: target is not exist or readable/IOError.'


def universal_save(target):
    """
    储存一个文件，自动在末尾添加空行，编码为 UTF-8
    :param target: 字典： {'文件全路径': ['文件内容']}
    无返回结果
    """
    for key, value in target.items():
        with open(key, "w", encoding="utf8") as file_object:
            for i in value:
                file_object.write(i)
            file_object.write('\n')
    print('文件输出完毕.')
