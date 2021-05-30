# 山灵M0播放器播放列表管理工具
# ver.7
# 列表可实现：随机化、排序、重命名
# By Clok Much
import sys

import config
import methods


from os import mkdir, listdir
from random import shuffle


# 检测设备路径，设定播放列表状态
while True:
    m0_device = methods.try_find_device()
    if type(m0_device) == str:
        print("检查到已导出的播放列表文件夹，无需自定义路径.")
        print(("当前设备盘符为：" + m0_device))
    elif type(m0_device) == list:
        print("检查到多个可能存在的设备，请自行选取路径.")
        m0_device = methods.get_a_dir(is_dir=False)
        if m0_device == 'Cancel':
            continue
        try:
            listdir(m0_device + config.Default.m0_folder + "\\")
        except FileNotFoundError:
            double_chk_result = methods.double_chk(title="操作确认",
                                                   content="所选驱动器不存在列表及列表文件夹，是否创建一个默认列表，从而添加音乐？（添加功能暂时没有）\n若不创建，需要再次选择驱动器.")
            if double_chk_result:
                mkdir(m0_device + config.Default.m0_folder)
            elif not double_chk_result:
                continue
        else:
            print(("选定的设备盘符为：" + m0_device))
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

    print("\n一切顺利，当前操作的盘符为 " + m0_device)
    # 若只有一个列表时，直接准备处理；若有多个列表，需自行选择需要处理的列表
    playlists = methods.get_all_files(m0_device + config.Default.m0_folder + "\\")
    if len(playlists) == 1:
        input("\n仅发现一个列表：" + playlists[0] + "\n按回车键开始处理本列表...")
        playlist = (m0_device + config.Default.m0_folder + "\\"
                    + playlists[0])
        playlist_editing = methods.analysis_a_playlist(playlist)
        while True:
            print("\n当前处理的播放列表为：" + playlist)
            print("当前列表对象数为：" + str(len(playlist_editing)))
            selection = methods.select_a_operation()
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
        if config.AutoOptCombine.switch:
            print(config.AutoOptCombine.note + " 功能已启用，正在执行功能...")
            combined_lists = []
            for name in playlists:
                if (config.AutoOptCombine.filename_suffix + config.Default.m0_playlist_type) in name:
                    combined_lists.append(name)
            print("找到疑似自动执行合成的播放列表文件：\n" + str(combined_lists))
            if combined_lists:
                source_songs = 0
                for tmp in combined_lists:
                    editing_combined_list = methods.analysis_a_playlist(m0_device + config.Default.m0_folder + "\\" + tmp)
                    if editing_combined_list[0] == config.AutoOptCombine.inct_in_file_line1 + "\n":
                        source_lists = editing_combined_list[1][2:-1].split(",")
                        combined_pool = []
                        for source_list in source_lists:
                            source_list_tmp = methods.analysis_a_playlist(m0_device + config.Default.m0_folder + "\\" + source_list + config.Default.m0_playlist_type)
                            source_songs += len(source_list_tmp)
                            combined_pool += source_list_tmp
                        if config.AutoOptCombine.combine_randomly:
                            # 设定随机重排合并列表时执行随机重排
                            print("随机重排合并后的播放列表...（此配置可在 config.py 中修改）")
                            shuffle(combined_pool)
                        combined_pool.insert(0, ("# " + ",".join(source_lists) + "\n"))
                        combined_pool.insert(0, (config.AutoOptCombine.inct_in_file_line1 + "\n"))
                        methods.output_a_playlist(combined_pool, m0_device + config.Default.m0_folder + "\\" + tmp)
                        print("自动合并完毕，详情如下：")
                        print("原始子列表共计 " + str(source_songs) + " 曲音频；")
                        print("自动合成的播放列表共计 " + str(len(combined_pool) - 2) + " 曲音频.")

        print("\n发现多个列表，请选择需要处理的列表...")
        playlist = methods.select_a_playlist(m0_device + config.Default.m0_folder)
        playlist_editing = methods.analysis_a_playlist(playlist)
        while True:
            print("\n当前处理的播放列表为：" + playlist)
            print("当前列表对象数为：" + str(len(playlist_editing)))
            selection = methods.select_a_operation()
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

    break
