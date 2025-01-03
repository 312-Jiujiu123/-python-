# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:25:36 2025

@author: Administrator
"""

for i in range(32): #输出32个
    ans = bin(1)[2:]   #bin(1)求1的二进制表示,结果是0b1,bin(1)[2:]是取bin[2]的值给ans
    if len(ans)!=5:  #ans值的长度少于5，在前面补0，凑够5位
        ans = '0'*(5-len(ans))+ans  #‘0’*出现次数，再加上前面提取的一位的1的二进制ans
    print(ans)
