 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random, easygui

secret = random.randint(1, 99)
guess = 0
tries = 0

easygui.msgbox("""你好，我是智能机器人，我有一个秘密！它是从1-99的数字，我会给你六
               次机会，看看你能不能猜对它！""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("你猜的是多少呢？")
    
    if not guess:
        break
   
    if guess < secret:
        easygui.msgbox(str(guess) + "你的数字太小了！")
    elif guess > secret:
        easygui.msgbox(str(guess) + "你的数字太大了！")
    
    tries += 1

if guess == secret:
    easygui.msgbox("你真的猜对了！太厉害了！")
else:
    easygui.msgbox("没有更多的机会啦！真实数字是" + str(secret))
    
    