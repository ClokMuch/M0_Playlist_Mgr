# 山灵 M0 播放列表管理工具

**注意：较美观的 GUI 遇到了一些困难，暂时不可用**


### 已实现功能
**当没有导出列表时：** 创建默认列表；

**当有导出列表时（支持多个列表批量处理）：**
1. 随机化列表；
2. 升序排列列表；
3. 创建副本列表；
4. 根据规则自动合并列表；
5. 启用或禁用列表；
6. 自动合并列表（仅对启用的列表生效）.

**当有受支持的其他软件导出的列表时（目前为 `.m3u8`, `.dpl`）：**
1. 自动转换盘符；
2. 自动转换为设备可识别的列表格式；
3. 自动删除原始导出列表（可配置为不删除：在 `config.py` 中：`class AutoOptTransform：remove_original_list` 对应的值，改为 `False` 即可）.

### 当前版本运行环境
建议 Microsoft Windows 7 及以上版本的操作系统；

Python 3.7 及以上版本（避免 `tkinter.filedialog.askopenfilenames()` 返回结果异常，已知某些版本 Python 会返回难以处理的结果）. 

### 使用方法
**直接使用（适用于 Windows 用户）**
1. 在 GitHub Release 界面中下载最新的版本（可能不是最新的代码）[（单击这里选择最新版本下载）](https://github.com/ClokMuch/M0_Playlist_Mgr/releases)

2. 连接山灵 M0 设备.

3. 找到下载到的可执行程序，并运行，按提示操作即可.

**运行开源代码（适用于已有 Python3 环境的 Windows 用户）：**
1. 下载仓库根目录的以下文件，并放在同一目录：
   
   &emsp;&emsp;`Application.py`, `methods.py`, `config.py`, `auto.py`, `actions.py`
   
   共 5 个文件.

2. 连接山灵 M0 设备.

3. 使用 Python 执行 *Application.py* 程序.

4. 按提示进行操作即可.
