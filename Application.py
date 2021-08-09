# 山灵M0播放器播放列表管理工具
# ver.11
# By Clok Much

from os import mkdir
from tkinter import Tk

import config
import methods
import auto
import actions

Tk().withdraw()

# 开始主循环
while True:
    print("*****开始运行*****")
    # 寻找/定位设备
    m0_device = methods.explore_devices()   # 尝试寻找设备
    if not m0_device:   # 没有找到设备
        print("无法自动找到设备")
        methods.showinfo(title="无法自动找到设备",
                         message="无法找到设备，可能是从未在设备中导出过列表.\n"
                                 "\n"
                                 "请您在接下来的选择器中，选择您的设备所在驱动器；\n"
                                 "如您选择了一个文件夹，将使用选取的文件夹所在的驱动器."
                         )
        m0_device = methods.get_a_dir(is_dir=False, tips='请选择一个驱动器...')
        print("选择的驱动器为：" + m0_device)
        print("即将创建占位空列表...")
        if not methods.double_chk(content="您选择的驱动器不包含任何可识别的列表，创建一个占位的空列表吗？\n"
                                          "\n"
                                          "如果不创建，您需要重新选择驱动器."):
            print("不创建占位空列表，重新选择驱动器...")
            print("**********************\n"
                  "*****重新开始运行*****\n"
                  "**********************")
            continue
        mkdir(m0_device + config.Default.m0_folder)     # 创建路径
        processing = {
            m0_device + config.Default.m0_folder +
            config.Default.playlist_default_name + config.Default.m0_playlist_type: '\n'
        }
        methods.universal_save(processing)  # 创建空列表
    elif len(m0_device) == 1:   # 仅单个设备时
        m0_device = m0_device[0]
    else:   # 多个识别到的设备时
        print("识别到多个设备：" + ', '.join(m0_device))
        methods.showinfo(title="识别到多个设备",
                         message="识别到多个设备，请您选择您需要处理的设备对应的驱动器.\n"
                                 "可选择的驱动器为：" + ', '.join(m0_device) + "\n"
                                 "\n"   
                                 "请您在接下来的选择器中，选择您需要处理的设备对应的驱动器；\n"
                                 "如您选择了一个文件夹，将使用选取的文件夹所在的驱动器；\n"
                                 "如果您选择了不支持的设备，您需要重新选择."
                         )
        m0_device = methods.get_a_dir(is_dir=False, tips='请选择需要处理的设备所在的驱动器，应当是：' +
                                                         ', '.join(m0_device) + ' 中的一个...')
    print("\n" +
          "*****一切顺利，当前操作的盘符为 " + m0_device + "*****\n")

    # 识别播放列表与准备
    playlists = methods.get_all_files(m0_device + config.Default.m0_folder + "\\")  # 载入列表目录的所有文件
    # 执行自动任务
    print("*****准备执行自动任务*****")
    auto.auto_opt_transform(playlists, m0_device)  # 自动任务：转换盘符
    auto.auto_opt_dpl_transform(playlists, m0_device)  # 自动任务：转换 .dpl 列表
    auto.auto_opt_combine(playlists, m0_device)  # 自动任务：合并列表
    print("*****自动任务执行完毕*****")
    print("刷新列表文件...")
    playlists = methods.get_all_files(m0_device + config.Default.m0_folder + "\\")  # 刷新目录的所有文件
    # 展示识别到的列表
    tmp_list = []   # 支持直接处理的列表
    tmp_disabled = []   # 停用的列表
    for playlist in playlists:
        if config.Default.m0_playlist_type in playlist:
            tmp_list.append(playlist)
        elif config.Default.m0_disabled_playlist in playlist:
            tmp_disabled.append(playlist)
    print("*****刷新完毕*****")
    if tmp_list:
        print("有 %s 个已启用的播放列表：" % (len(tmp_list)))
        for i in tmp_list[:-1]:
            print(i, end=', ')
        print(tmp_list[-1] + '.')
        if len(tmp_list) > config.Default.number_of_playlist:
            print("请注意：当前启用的播放列表数量较多，可能不便于使用，建议控制启用的播放列表数量不超过 " +
                  str(config.Default.number_of_playlist) + " .")
    if tmp_disabled:
        print("有 %s 个禁用的播放列表：" % (len(tmp_disabled)))
        for i in tmp_disabled[:-1]:
            print(i, end=', ')
        print(tmp_disabled[-1] + '.')
    del tmp_list, tmp_disabled  # 清除临时变量，回收内存
    # 将列表路径补全
    for i in range(len(playlists)):
        playlists[i] = m0_device + config.Default.m0_folder + playlists[i]
    # 处理播放列表
    if len(playlists) == 1:
        # 单个列表的情况
        while True:
            print("\n当前处理的列表为：" + playlists[0])
            processing = methods.analysis_playlist(playlists)
            for key, value in processing.items():
                if key[key.rfind('.'):] == config.Default.m0_disabled_playlist:
                    print("▲ 注意：当前选定的列表是冻结/禁用状态 ▲")
                print("处理的列表包含曲目数量为 " + str(len(value)) + '.')
            # 开始交互操作
            selection = methods.universal_selections(selections=config.Operations.Single.details)
            processing = actions.start_action(processing, selection)
            print("*****操作完毕*****")
            playlists = []
            for key in processing.keys():
                playlists.append(key)
    else:
        # 多个列表的情况
        playlists = methods.select_playlist(m0_device + config.Default.m0_folder)
        if len(playlists) == 1:     # 多个列表选择单个列表时，与上代码一致
            # 单个列表的情况
            while True:
                print("\n当前处理的列表为：" + playlists[0])
                processing = methods.analysis_playlist(playlists)
                for key, value in processing.items():
                    if key[key.rfind('.'):] == config.Default.m0_disabled_playlist:
                        print("▲ 注意：当前选定的列表是冻结/禁用状态 ▲")
                    print("处理的列表包含曲目数量为 " + str(len(value)) + '.')
                # 开始交互操作
                selection = methods.universal_selections(selections=config.Operations.Single.details)
                processing = actions.start_action(processing, selection)
                print("*****操作完毕*****")
                playlists = []
                for key in processing.keys():
                    playlists.append(key)
        else:
            while True:
                print("\n当前选定列表数量为：" + str(len(playlists)) + " ，为：")
                for playlist in playlists:
                    print('    ' + playlist)
                processing = methods.analysis_playlist(playlists)
                num = 0     # 统计总曲目数量
                for value in processing.values():
                    num += len(value)
                print("处理的列表包含曲目数量为 " + str(num) + '.')
                # 开始交互操作
                selection = methods.universal_selections(selections=config.Operations.More.details)
                processing = actions.start_action(processing, selection)
                print("*****操作完毕*****")
                playlists = []
                for key in processing.keys():
                    playlists.append(key)
