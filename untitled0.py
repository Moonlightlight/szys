# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:04:29 2018

@author: Administrator
"""

import random #要产生随机数
ysf = ['＋','－','×','÷'] #运算符
jg = '0'
print('Input "js" Quit') #输入0000后退出
while True:
    fh = random.randint(0, 3)
    n1 = random.randint(1, 100) #数1
    n2 = random.randint(1, 100) #数2
    jsz = 0 #计算得到的数值
    if fh == 0: #相加
        jsz = n1 + n2
    elif fh == 1: #相减
        n1,n2 = max(n1,n2),min(n1,n2)
        jsz = n1 - n2
    elif fh == 2: #相乘
        jsz = n1 * n2
    elif fh == 3: #相除
        n1,n2 = max(n1,n2),min(n1,n2)
        while n1 % n2 != 0:
            n1 = random.randint(1, 100)
            n2 = random.randint(1, 100)
            n1,n2 = max(n1,n2),min(n1,n2)
        jsz = int(n1 / n2)
 
    print(n1, ysf[fh], n2, '= ', end='')
    
    jg = input()
    if jg == 'js':
        break
    sr = int(jg)
    if int(sr) == jsz:
        print('答案正确')
    else:
        print('计算错了. 正确的答案是', jsz)