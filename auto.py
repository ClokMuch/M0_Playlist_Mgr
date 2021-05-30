# 山灵M0播放器播放列表管理工具自动执行方法库
# ver.7
# By Clok Much

import methods
import config

from random import shuffle
from os import remove


def auto_opt_combine(playlists, m0_device):
    # 自动合并列表
    if config.AutoOptCombine.switch:
        print(config.AutoOptCombine.note + " 功能已启用，正在执行功能...")
        combined_lists = []
        for name in playlists:
            if ((config.AutoOptCombine.filename_suffix + config.Default.m0_playlist_type) in name) and \
                    (config.AutoOptCombine.filename_mid in name):
                combined_lists.append(name)
        if combined_lists:
            print("找到疑似自动执行合成的播放列表文件：\n" + str(combined_lists))
            source_songs = 0
            for tmp in combined_lists:
                editing_combined_list = methods.analysis_a_playlist(m0_device + config.Default.m0_folder + "\\" + tmp)
                if editing_combined_list[0] == config.AutoOptCombine.inct_in_file_line1 + "\n":
                    source_lists = editing_combined_list[1][2:-1].split(",")
                    combined_pool = []
                    for source_list in source_lists:
                        source_list_tmp = methods.analysis_a_playlist(
                            m0_device + config.Default.m0_folder + "\\" + source_list + config.Default.m0_playlist_type)
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
        else:
            print("无满足自动执行条件的对象.")


def auto_opt_transform(playlists, m0_device, ):
    # 自动转换盘符
    if config.AutoOptTransform.switch:
        print(config.AutoOptTransform.note + " 功能已启用，正在执行功能...")
        pre_transform_lists = []
        transform_lists = []
        for name in playlists:
            if config.AutoOptTransform.file_type in name:
                pre_transform_lists.append(name)
        if pre_transform_lists:
            for tmp in pre_transform_lists:
                editing_pre_transform_list = \
                    methods.analysis_a_playlist(m0_device + config.Default.m0_folder + "\\" + tmp)
                try:
                    if config.AutoOptTransform.inct_in_file_line1 in editing_pre_transform_list[0]:
                        transform_lists.append(tmp)
                except IndexError:
                    continue
            if transform_lists:
                print("找到疑似可转换的列表：\n" + str(transform_lists))
                for transform_list in transform_lists:
                    original_list = methods.analysis_a_playlist(m0_device + config.Default.m0_folder + "\\" +
                                                                transform_list)
                    output_list = []
                    del original_list[0]
                    replace_prefix_num = 0
                    for tmp in original_list:
                        if (tmp[1] == ':') and (tmp[2] == '\\'):
                            tmp = config.Default.m0_prefix[0] + tmp[1:]
                            replace_prefix_num += 1
                        output_list.append(tmp)
                    print("对列表 " + transform_list + "已完成 " + str(replace_prefix_num) + " 个列表内的盘符指向.")
                    methods.output_a_playlist(output_list, m0_device + config.Default.m0_folder + "\\" +
                                              transform_list[0:-5] + config.Default.m0_playlist_type)
                    if config.AutoOptTransform.remove_original_list:
                        remove(m0_device + config.Default.m0_folder + "\\" + transform_list)
                        print("已删除转换前的列表文件. （可在 config.py 中修改配置）")
                print("自动转换盘符完毕.\n")
            else:
                print("无满足自动执行条件的对象.")
