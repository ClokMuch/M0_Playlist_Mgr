# 山灵M0播放器播放列表管理工具自动执行方法库
# ver.10
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
        result = {}
        for name in playlists:
            if ((config.AutoOptCombine.filename_suffix + config.Default.m0_playlist_type) in name) and \
                    (config.AutoOptCombine.filename_mid in name):
                combined_lists.append(name)
        if combined_lists:
            print("找到疑似自动执行合成的播放列表文件：\n" + str(combined_lists))
            for combined_list in combined_lists:
                # 每个合并列表的循环 'ApeAndDefault#AutoCombine.m3u'
                source_songs = 0
                source_lists = combined_list[
                               :-len(config.AutoOptCombine.filename_suffix + config.Default.m0_playlist_type)
                               ].split(config.AutoOptCombine.filename_mid)
                combined_pool = []
                for source_list in source_lists:  # ['Ape', 'Default']
                    try:
                        source_list_tmp = methods.universal_analysis(
                            m0_device + config.Default.m0_folder + source_list + config.Default.m0_playlist_type
                        )
                    except IOError:
                        if config.AutoOptCombine.combine_disabled:
                            source_list_tmp = methods.universal_analysis(
                                m0_device + config.Default.m0_folder + source_list + config.Default.m0_disabled_playlist
                            )
                            print("子列表 " + source_list + " 为禁用状态，但仍将合并（可在 config.py 中修改设置）.")
                        else:
                            print("子列表 " + source_list + " 为禁用状态，不参与合并（可在 config.py 中修改设置）.")
                            continue
                    source_songs += len(source_list_tmp[1])
                    combined_pool += source_list_tmp[1]
                if config.AutoOptCombine.combine_randomly:
                    # 设定随机重排合并列表时执行随机重排
                    print("随机重排合并后的播放列表...（可在 config.py 中修改设置）")
                    shuffle(combined_pool)
                result[m0_device + config.Default.m0_folder + combined_list] = combined_pool
                print(combined_list + " 自动合并完毕，参与合并的子列表共计 " + str(source_songs) + " 曲；")
                print("自动合成的播放列表共计 " + str(len(combined_pool)) + " 曲.\n")
            methods.universal_save(result)
            print("自动合并全部完毕，共处理自动合并列表数量为：" + str(len(combined_lists)) + '.')
        else:
            print("无满足自动执行条件的对象，不进行处理.\n")


def auto_opt_transform(playlists, m0_device):
    # 自动转换盘符
    if config.AutoOptTransform.switch:
        print(config.AutoOptTransform.note + " 功能已启用，正在执行功能...")
        pre_transform_lists = []
        transform_lists = []
        for name in playlists:
            if config.AutoOptTransform.file_type in name:
                pre_transform_lists.append(name)
        if pre_transform_lists:
            # 补全路径
            for i in range(len(pre_transform_lists)):
                pre_transform_lists[i] = m0_device + config.Default.m0_folder + pre_transform_lists[i]
            original = methods.analysis_playlist(pre_transform_lists)
            for key, value in original.items():
                try:
                    if config.AutoOptTransform.inct_in_file_line1 in value[0]:
                        transform_lists.append(key)
                    else:
                        continue
                except IndexError:
                    continue
                else:
                    continue
            if transform_lists:
                print("找到 " + str(len(transform_lists)) + " 个疑似可转换的列表：")
                for transform_list in transform_lists:
                    print("    " + transform_list)
                result = {}
                for key, value in original.items():
                    del value[0]  # 删除首行文件标记
                    replace_num = 0
                    new_key = key[:key.rfind('.')] + config.Default.m0_playlist_type
                    new_value = []
                    for tmp in value:
                        if tmp[:len(config.Default.m0_prefix)] != config.Default.m0_prefix:
                            new_value.append(config.Default.m0_prefix + tmp[len(config.Default.m0_prefix):])
                            replace_num += 1
                        else:
                            new_value.append(tmp)
                    result[new_key] = new_value
                    print("对列表 " + key + "已完成 " + str(replace_num) + " 个列表内的盘符指向.")
                methods.universal_save(result)
                del result
                if config.AutoOptTransform.remove_original_list:
                    del_num = 0
                    for key in original.keys():
                        remove(key)
                        del_num += 1
                    print("已删除转换前的 %s 个列表文件. （可在 config.py 中修改配置）" % del_num)
            print("自动转换盘符完毕.\n")
        else:
            print("无满足自动执行条件的对象，不进行处理.\n")


def auto_opt_dpl_transform(playlists, m0_device):
    # 自动转换 .dpl 播放列表
    if config.AutoOptDplTransform.switch:
        print(config.AutoOptDplTransform.note + " 功能已启用，正在执行功能...")
        pre_transform_lists = []
        transform_lists = []
        for name in playlists:
            if config.AutoOptDplTransform.file_type in name:
                pre_transform_lists.append(name)
        if pre_transform_lists:
            # 补全路径
            for i in range(len(pre_transform_lists)):
                pre_transform_lists[i] = m0_device + config.Default.m0_folder + pre_transform_lists[i]
            original = methods.analysis_playlist(pre_transform_lists)
            for key, value in original.items():
                try:
                    if config.AutoOptDplTransform.inct_in_file_line1 in value[0]:
                        transform_lists.append(key)
                    else:
                        continue
                except IndexError:
                    continue
                else:
                    continue
            if transform_lists:
                print("找到 " + str(len(transform_lists)) + " 个疑似可转换的列表：")
                for transform_list in transform_lists:
                    print("    " + transform_list)
                result = {}
                for key, value in original.items():
                    del value[0]  # 删除首行文件标记
                    replace_num = 0
                    all_num = 0
                    new_key = key[:key.rfind('.')] + config.Default.m0_playlist_type
                    new_value = []
                    for tmp in value:
                        if config.AutoOptDplTransform.inct_inner in tmp:
                            tmp = tmp[
                                  (tmp.rfind(config.AutoOptDplTransform.inct_inner) +
                                   len(config.AutoOptDplTransform.inct_inner)):]
                            all_num += 1
                            if tmp[:len(config.Default.m0_prefix)] != config.Default.m0_prefix:
                                new_value.append(config.Default.m0_prefix + tmp[len(config.Default.m0_prefix):])
                                replace_num += 1
                        else:
                            new_value.append(tmp)
                    result[new_key] = new_value
                    print("对列表 " + key + "已完成 " + str(replace_num) + " 个列表内的盘符指向，"
                                                                     "列表包含曲目数量为：" + str(all_num))
                methods.universal_save(result)
                del result
                if config.AutoOptDplTransform.remove_original_list:
                    del_num = 0
                    for key in original.keys():
                        remove(key)
                        del_num += 1
                    print("已删除转换前的 %s 个列表文件. （可在 config.py 中修改配置）" % del_num)
            print("转换 .dpl 格式及盘符指向完毕.\n")
        else:
            print("无满足自动执行条件的对象，不进行处理.\n")
