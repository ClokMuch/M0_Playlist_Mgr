# 山灵M0播放器播放列表管理工具配置
# ver.11
# By Clok Much

class Default:
    m0_prefix = "A:\\"  # M0播放列表的驱动器映射
    m0_folder = "_explaylist_data\\"  # M0播放列表所在的文件夹，以 \\ 结尾
    m0_playlist_type = ".m3u"   # M0播放列表文件格式
    m0_disabled_playlist = ".m0disabled"    # M0禁用的播放列表格式
    playlist_default_name = "Default"   # 默认播放列表名称
    support_file_type = [".m3u", ".m3u8", ".dpl"]   # 本工具支持的文件格式
    support_music_types = [".mp3", ".flac", ".wav"]   # 支持的音乐文件名
    number_of_playlist = 6  # 启用的播放列表数量建议，当超过本数值时在控制台输出提醒


class AutoOptCombine:
    note = "自动合并列表"
    switch = True   # 功能开关
    combine_randomly = True  # 自动合并后打乱列表
    combine_disabled = True  # 子列表停用时仍然合并
    # 作用条件
    # inct_in_file_line1 = '#auto_opt_combine'    # 文件第一行标记，暂时废弃
    filename_prefix = ''    # 合并列表的文件名前缀
    filename_mid = 'And'    # 合并列表文件名中分割原始列表的连接
    filename_suffix = '#AutoCombine'    # 合并列表文件名后缀


class AutoOptTransform:
    note = "转换 .m3u8 "
    remove_original_list = True    # 自动删除原始列表
    # clear_sig = True    # 去除某些带BOM的列表前缀
    switch = True
    # 作用条件
    inct_in_file_line1 = '#EXTM3U8'    # 文件第一行标记
    file_type = '.m3u8'   # 处理的扩展名


class AutoOptDplTransform:
    note = "转换 .dpl "
    remove_original_list = True  # 自动删除原始列表
    switch = True
    # 作用条件
    inct_in_file_line1 = 'DAUMPLAYLIST'  # 文件第一行标记
    inct_inner = '*file*'  # 行内提示文件路径的标记
    file_type = '.dpl'  # 处理的扩展名


class Operations:

    class Actions:
        # 支持的内部命令
        actions = ('lst_copy', 'lst_switch', 'lst_disable', 'lst_enable', 'lst_rename', 'lst_random',
                   'lst_order', 'lst_exit')

    class Single:
        details = {
            '1': ('随机化', 'lst_random'),
            '2': ('升序排序', 'lst_order'),
            '3': ('创建列表副本（不删除旧列表，继续编辑旧列表）', 'lst_copy'),
            '4': ('重命名当前列表，并继续编辑当前列表', 'lst_rename'),
            '0': ('切换当前列表状态（启用或禁用）', 'lst_switch'),
            '6': ('退出程序', 'lst_exit')
        }   # 单个播放列表处理项目

    class More:
        details = {
            '1': ('全部随机化', 'lst_random'),
            '2': ('全部升序排序', 'lst_order'),
            '+': ('将选定的列表全设为启用状态', 'lst_enable'),
            '-': ('将选定的列表全设为禁用状态', 'lst_disable'),
            '0': ('对调选定的列表状态（启用变为禁用，禁用变为启用）', 'lst_switch'),
            '6': ('退出程序', 'lst_exit')
        }   # 多个播放列表处理项目
