# 山灵M0播放器播放列表管理工具配置
# ver.9
# By Clok Much

class Default:
    m0_prefix = "A:\\"  # M0播放列表的驱动器映射
    m0_folder = "_explaylist_data"  # M0播放列表所在的文件夹
    m0_playlist_type = ".m3u"   # M0播放列表文件格式
    playlist_default_name = "Default"   # 默认播放列表名称
    support_file_type = [".m3u", ".m3u8"]   # 本工具支持的文件格式
    support_music_types = [".mp3", ".flac", ".wav"]   # 支持的音乐文件名


class AutoOptCombine:
    note = "自动合并列表"
    switch = True   # 功能开关
    combine_randomly = True  # 自动合并后打乱列表
    # 作用条件
    # inct_in_file_line1 = '#auto_opt_combine'    # 文件第一行标记，暂时废弃
    filename_prefix = ''    # 合并列表的文件名前缀
    filename_mid = 'And'    # 合并列表文件名中分割原始列表的连接
    filename_suffix = '#AutoCombine'    # 合并列表文件名后缀


class AutoOptTransform:
    note = "自动转换本工具支持的格式为M0播放列表为文件格式"
    remove_original_list = True    # 自动删除原始列表
    # clear_sig = True    # 去除某些带BOM的列表前缀
    switch = True
    # 作用条件
    inct_in_file_line1 = '#EXTM3U8'    # 文件第一行标记
    file_type = '.m3u8'   # 处理的扩展名


class Operations:
    single = {
        '1': '随机化',
        '2': '升序排序',
        '3': '创建列表副本（不删除旧列表，继续编辑旧列表）',
        '4': '退出程序'
    }   # 单个播放列表处理项目
    more = {
        '1': '全部随机化',
        '2': '全部升序排序',
        '3': '退出程序'
    }   # 多个播放列表处理项目
