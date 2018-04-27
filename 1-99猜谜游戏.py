# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random, easygui

easygui.msgbox("让我们来玩一个游戏！")

name = easygui.enterbox("请输入你的姓名：")
city = easygui.enterbox("请输入你的房间号、街道、城市：")
provice = easygui.enterbox("请输入你的省、地区、州：")
code = easygui.enterbox("请输入你的邮政编码：")

easygui.msgbox("信的地址为：\n" + name + "\n" + city + "\n" + provice + "\n" + code)
