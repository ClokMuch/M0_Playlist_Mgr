# 山灵M0播放器播放列表管理工具
# ver.1
# 实现播放列表 Default 的随机化
# By Clok Much

import config
import methods

from os import mkdir
from random import shuffle


# 检测设备路径，设定播放列表状态
m0_device = methods.chk_if_device()
if not m0_device:
    playlist_loop_inct = False
    double_chk_result = False
    while not playlist_loop_inct:
        m0_device = methods.get_a_dir(is_dir=False)
        # 如果指定了一个驱动器，说明播放器未曾导出过播放列表，因此需要创建一个播放列表存放的文件夹
        double_chk_result = methods.double_chk(title="操作确认", content="所选驱动器不存在列表及列表文件夹，是否创建？\n若不创建，需要再次选择驱动器.")
        if double_chk_result:
            mkdir(m0_device + config.Default.m0_folder)
            playlist_loop_inct = True

exist_playlist = methods.chk_if_playlist(m0_device)

# 合并播放列表的完整路径：Default.m3u
if exist_playlist == ("Default" or True):
    playlist = (m0_device + config.Default.m0_folder + "\\"
                + config.Default.playlist_default_name
                + config.Default.m0_playlist_type)
elif not exist_playlist:
    playlist = (m0_device + config.Default.m0_folder + "\\"
                + config.Default.playlist_default_name
                + config.Default.m0_playlist_type)
    with open(playlist, "w", encoding="utf8") as file_object:
        file_object.write("Default")
        print("创建了一个Default播放列表")
else:
    playlist = "coming_soon"  # 其他列表将在后续支持

# 默认播放列表：读取、随机化、保存
if playlist == "coming_soon":
    print("暂不支持非Default的列表处理、暂不支持创建新列表")
else:
    with open(playlist, "r", encoding="utf8") as file_obj:
        tmp = file_obj.readlines()
        tmp[-1] = tmp[-1] + '\n'
        shuffle(tmp)
    with open(playlist, "w", encoding="utf8") as file_obj:
        for i in tmp:
            file_obj.write(i)
