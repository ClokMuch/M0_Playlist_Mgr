class Default:
    m0_prefix = "A:\\"  # M0播放列表的驱动器映射
    m0_folder = "_explaylist_data"  # M0播放列表所在的文件夹
    m0_playlist_type = ".m3u"   # M0播放列表文件格式
    playlist_default_name = "Default"   # 默认播放列表名称
    support_file_type = [".m3u", ".m3u8"]   # 本工具支持的文件格式
    support_music_types = [".mp3", ".flac", ".wav"]   # 支持的音乐文件名


class AutoOptCombine:
    note = "自动合并列表"
    switch = True   # 自动合并指定的播放列表
    combine_randomly = True  # 自动合并后打乱列表
    inct_in_file_line1 = '# auto_opt_combine'    # 文件第一行标记
    filename_prefix = ''    # 合并列表的文件名前缀
    filename_mid = 'And'    # 合并列表文件名中分割原始列表的连接
    filename_suffix = '#AutoCombine'    # 合并列表文件名后缀
