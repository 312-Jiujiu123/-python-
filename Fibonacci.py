# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:43:53 2025

@author: Administrator

problem: Fivonacci

number:1
"""
n = int(input());#输入最大的Fibnacci数的最大个数
F=[1,1]#初始化Fibonacci数列,第一个和第二个数是1
for i in range(2,n):#将Fibonacci数F[2]到F[n-1]
    F.append((F[i-2]+F[i-1])%10007)
print(F)
