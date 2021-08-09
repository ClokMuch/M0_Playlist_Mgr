# 山灵M0播放器播放列表管理工具选项执行库
# ver.11
# By Clok Much
from sys import exit
from os import system as shell
from os.path import exists
from random import shuffle

import config
import methods


def start_action(target, action):
    # 开始执行，target 为解析播放列表的字典， action 为内部命令字符串
    # target: {'full_path': ['content']}
    if action == 'lst_random':
        return lst_random(target)
    elif action == 'lst_order':
        return lst_order(target)
    elif action == 'lst_rename':
        return lst_rename(target)
    elif action == 'lst_copy':
        return lst_copy(target)
    elif action == 'lst_switch':
        return lst_switch(target)
    elif action == 'lst_disable':
        return lst_disable(target)
    elif action == 'lst_enable':
        return lst_enable(target)
    elif action == 'lst_exit':
        exit()
    else:
        print('#InnerError:actions.start_action: action is not exist.')
        return '#InnerError:actions.start_action: action is not exist.'


def lst_random(target):
    # 随机化输入的字典值列表，返回字典
    for value in target.values():
        shuffle(value)
    methods.universal_save(target)
    return target


def lst_order(target):
    # 升序排序输入的字典值列表，返回字典
    for value in target.values():
        value.sort()
    methods.universal_save(target)
    return target


def lst_copy(target):
    # 创建列表副本（不删除旧列表，继续编辑旧列表）
    # 复制操作只在操作单个列表时显示，故内部将字典键转换为列表进行操作，返回原始的字典
    if len(target) != 1:  # 避免内部错误，当应用到多列表时产生异常
        print('#InnerError:actions.lst_copy: input dict len is not 1.')
        return '#InnerError:actions.lst_copy: input dict len is not 1.'
    tmp = []
    for key in target.keys():
        tmp.append(key)
    tmp = tmp[0]
    while True:
        new_name = input('请输入新的播放列表名称（不包含扩展名）：') + tmp[tmp.rfind('.'):]
        if exists(tmp[:tmp.rfind('\\')] + new_name):
            print("您输入的文件名已存在，请再次输入另一个名字！")
        else:
            print('copy "' + tmp + '" "' + tmp[:tmp.rfind('\\')+1] + new_name + '"')
            shell('copy "' + tmp + '" "' + tmp[:tmp.rfind('\\')+1] + new_name + '"')
            input(new_name + "为创建的副本的文件全名，按回车键继续...")
            return target


def lst_rename(target):
    # 重命名当前列表，并编辑当前列表
    if len(target) != 1:  # 避免内部错误，当应用到多列表时产生异常
        print('#InnerError:actions.lst_rename: input dict len is not 1.')
        return '#InnerError:actions.lst_rename: input dict len is not 1.'
    tmp = []
    for key in target.keys():
        tmp.append(key)
    tmp = tmp[0]
    while True:
        new_name = input('请输入新的播放列表名称（不包含扩展名）：') + tmp[tmp.rfind('.'):]
        if exists(tmp[:tmp.rfind('\\')] + new_name):
            print("您输入的文件名已存在，请再次输入另一个名字！")
        ini_pool = ('\\', '/', ':', '*', '?', '"', '<', '>', '|')
        chk_result = []
        for i in new_name:
            if i in ini_pool:
                chk_result.append(i)
        if chk_result:
            print("您输入的文件名含有不可在系统重命名的字符：", end='')
            for i in chk_result:
                print(i, end=' ')
            print("，请您再次输入另一个名字！")
        else:
            print('rename "' + tmp + '" "' + new_name + '"')
            shell('rename "' + tmp + '" "' + new_name + '"')
            target[tmp[:tmp.rfind('\\')+1] + new_name] = target.pop(tmp)  # 更新字典键
            input(new_name + "为重命名后的文件全名，按回车键继续操作这个列表...")
            return target


def lst_switch(target):
    # 切换当前列表状态
    result = {}
    for key in target.keys():
        if key[key.rfind('.'):] == config.Default.m0_playlist_type:  # 列表为启用状态，将切换为禁用状态
            shell('rename "' + key + '" "' + key[
                                             key.rfind('\\') + 1:key.rfind('.')] + config.Default.m0_disabled_playlist +
                  '"')
            tmp = key[:key.rfind('.')] + config.Default.m0_disabled_playlist
            result[tmp] = target[key]
        else:  # 列表为禁用状态，将切换为启用状态
            shell('rename "' + key + '" "' + key[key.rfind('\\') + 1:key.rfind('.')] + config.Default.m0_playlist_type +
                  '"')
            tmp = key[:key.rfind('.')] + config.Default.m0_playlist_type
            result[tmp] = target[key]
    return result


def lst_disable(target):
    # 禁用选定的列表
    result = {}
    for key in target.keys():
        if key[key.rfind('.'):] == config.Default.m0_playlist_type:  # 列表为启用状态，将切换为禁用状态
            shell(
                'rename "' + key + '" "' + key[
                                           key.rfind('\\') + 1:key.rfind('.')] + config.Default.m0_disabled_playlist +
                '"')
            tmp = key[:key.rfind('.')] + config.Default.m0_disabled_playlist
            result[tmp] = target[key]
        else:  # 列表为禁用状态，不变
            result[key] = target[key]
    return result


def lst_enable(target):
    # 启用选定的列表
    result = {}
    for key in target.keys():
        if key[key.rfind('.'):] == config.Default.m0_playlist_type:  # 列表为启用状态，不变
            result[key] = target[key]
        else:  # 列表为禁用状态，将切换为启用状态
            shell('rename "' + key + '" "' + key[key.rfind('\\') + 1:key.rfind('.')] + config.Default.m0_playlist_type +
                  '"')
            tmp = key[:key.rfind('.')] + config.Default.m0_playlist_type
            result[tmp] = target[key]
    return result
