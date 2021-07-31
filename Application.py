# 山灵M0播放器播放列表管理工具
# ver.7
# By Clok Much
import sys
from os import mkdir, listdir
from random import shuffle
from tkinter import Tk

import config
import methods
import auto

Tk().withdraw()

while True:
    m0_device = methods.try_find_device()   # 尝试寻找设备
    if type(m0_device) == str:
        # 返回类型为单个 str ，表示只找到一个设备
        print("检查到已导出的播放列表文件夹，无需自定义路径.")
        print(("当前设备盘符为：" + m0_device))
    elif type(m0_device) == list:
        # 返回类型为 list ，表示找到多个设备
        print("检查到多个可能存在的设备，请自行选取路径.")
        m0_device = methods.get_a_dir(is_dir=False)
        if m0_device == 'Cancel':
            continue
        try:
            listdir(m0_device + config.Default.m0_folder + "\\")
        except FileNotFoundError:
            double_chk_result = methods.double_chk(title="操作确认",
                                                   content="所选驱动器不存在列表及列表文件夹，是否创建一个默认列表，\
                                                           从而添加音乐？（添加功能暂时没有）\n若不创建，需要再次选\
                                                           择驱动器.")
            if double_chk_result:
                mkdir(m0_device + config.Default.m0_folder)
            elif not double_chk_result:
                continue
        else:
            print(("选定的设备盘符为：" + m0_device))
    elif not m0_device:
        # 值返回为 False ，表示没有查找到设备
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
    print("\n一切顺利，当前操作的盘符为 " + m0_device)
    # 若只有一个列表时，直接准备处理；若有多个列表，需自行选择需要处理的列表
    playlists = methods.get_all_files(m0_device + config.Default.m0_folder + "\\")
    if len(playlists) == 1:
        # 单个列表的情况
        auto.auto_opt_transform(playlists, m0_device)  # 自动任务：转换盘符
        playlists[0] = playlists[0][:-5] + config.Default.m0_playlist_type
        print("仅发现一个列表：" + playlists[0])
        playlist = (m0_device + config.Default.m0_folder + "\\"
                    + playlists[0])
        playlist_editing = methods.analysis_playlist(playlist)
        while True:
            print("\n当前处理的播放列表为：" + playlist)
            print("当前列表对象数为：" + str(len(playlist_editing)))
            selection = methods.universal_selections(selections=config.Operations.single)
            if selection == 1:
                shuffle(playlist_editing)
                methods.output_a_playlist(playlist_editing, playlist)
                input(playlists[0] + " 列表随机化完毕，按回车键继续...")
                continue
            elif selection == 2:
                playlist_editing.sort()
                methods.output_a_playlist(playlist_editing, playlist)
                input(playlists[0] + " 列表升序排列完毕，按回车键继续...")
                continue
            elif selection == 3:
                playlist_editing.sort(reverse=True)
                new_name = input('请输入新的播放列表名称（不包含扩展名）：')
                methods.output_a_playlist(playlist_editing, m0_device + config.Default.m0_folder + "\\"
                                          + new_name + config.Default.m0_playlist_type)
                input(new_name + config.Default.m0_playlist_type + "为新修正的全文件名，按回车键继续...")
                continue
            elif selection == 4:
                sys.exit()

    elif len(playlists) >= 2:
        auto.auto_opt_transform(playlists, m0_device)   # 自动任务：转换盘符
        auto.auto_opt_combine(playlists, m0_device)     # 自动任务：合并列表
        print("\n发现多个列表，请选择需要处理的列表，可以选择一个或多个列表...")
        # ▲已知问题：包含同名不同类型列表，自动转换后只有一个M0支持列表时仍提示多个列表
        playlist = methods.select_playlist(m0_device + config.Default.m0_folder)
        playlist_editing = methods.analysis_playlist(playlist)
        print(len(playlist_editing))
        if len(playlist_editing) == 1:
            playlist = playlist[0]
            playlist_editing = playlist_editing[0]
            while True:
                print("\n当前处理的播放列表为：" + playlist)
                print("当前列表对象数为：" + str(len(playlist_editing)))
                selection = methods.universal_selections(selections=config.Operations.single)
                if selection == 1:
                    shuffle(playlist_editing)
                    methods.output_a_playlist(playlist_editing, playlist)
                    input(playlist + " 列表随机化完毕，按回车键继续...")
                    continue
                elif selection == 2:
                    playlist_editing.sort()
                    methods.output_a_playlist(playlist_editing, playlist)
                    input(playlist + " 列表升序排列完毕，按回车键继续...")
                    continue
                elif selection == 3:
                    playlist_editing.sort(reverse=True)
                    new_name = input('请输入新的播放列表名称（不包含扩展名）：')
                    methods.output_a_playlist(playlist_editing, m0_device + config.Default.m0_folder + "\\"
                                              + new_name + config.Default.m0_playlist_type)
                    input(new_name + config.Default.m0_playlist_type + "为新修正的全文件名，按回车键继续...")
                    continue
                elif selection == 4:
                    sys.exit()
        else:
            while True:
                print("\n当前处理的播放列表有" + str(len(playlist_editing)) + "个，为：")
                num = 1
                all_songs = 0
                for i in playlist_editing.keys():
                    print(str(num) + "@" + i)
                    num += 1
                    all_songs += len(playlist_editing[i])
                print("所有列表曲目总和为：" + str(all_songs))
                selection = methods.universal_selections(selections=config.Operations.more)
                if selection == 1:
                    for i in playlist_editing.keys():
                        shuffle(playlist_editing[i])
                        methods.output_a_playlist(playlist_editing[i], i)
                    input("全部列表随机化完毕，按回车键继续...")
                    continue
                elif selection == 2:
                    for i in playlist_editing.keys():
                        playlist_editing[i].sort()
                        methods.output_a_playlist(playlist_editing[i], i)
                    input("全部列表升序排列完毕，按回车键继续...")
                    continue
                elif selection == 3:
                    sys.exit()

    break
