# 山灵M0播放器播放列表管理工具
# ver.4
# 尝试随机化任意一个列表（自选）
# By Clok Much

import config
import methods


from os import mkdir
from random import shuffle


# 检测设备路径，设定播放列表状态
while True:
    m0_device = methods.try_find_device()
    if m0_device:
        print("检查到已导出的播放列表文件夹，无需自定义路径.")
        print(("当前设备盘符为：" + m0_device))
    elif not m0_device:
        print("无法检索到设备，可能是从未导出过播放列表，请自行选取设备路径.")
        m0_device = methods.get_a_dir(is_dir=False)
        if m0_device == 'Cancel':
            continue
        # 如果指定了一个驱动器，说明播放器未曾导出过播放列表，因此需要创建一个播放列表存放的文件夹
        double_chk_result = methods.double_chk(title="操作确认",
                                               content="所选驱动器不存在列表及列表文件夹，是否创建一个默认列表，从而添加音乐？（添加功能暂时没有）\n若不创建，需要再次选择驱动器.")
        if double_chk_result:
            mkdir(m0_device + config.Default.m0_folder)

        elif not double_chk_result:
            continue

    print("一切顺利，当前操作的盘符为 " + m0_device)
    # 若只有一个列表时，直接准备处理；若有多个列表，需自行选择需要处理的列表
    playlists = methods.get_all_files(m0_device + config.Default.m0_folder + "\\")
    if len(playlists) == 1:
        input("仅发现一个列表：" + playlists[0] + "\n按回车键开始随机化这个列表...")
        playlist = (m0_device + config.Default.m0_folder + "\\"
                    + playlists[0])
        playlist_editing = methods.analysis_a_playlist(playlist)
        shuffle(playlist_editing)
        methods.output_a_playlist(playlist_editing, playlist)
        input(playlists[0] + " 列表随机化完毕.")

    elif len(playlists) >= 2:
        print("发现多个列表，请选择需要处理的列表...")
        playlist = methods.select_a_playlist(m0_device + config.Default.m0_folder)
        playlist_editing = methods.analysis_a_playlist(playlist)
        shuffle(playlist_editing)
        methods.output_a_playlist(playlist_editing, playlist)
        input(playlists[0] + " 列表随机化完毕.")

    break
