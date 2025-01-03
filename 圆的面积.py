# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:04:48 2025

@author: Administrator

number:2

problem:圆的面积
"""
import math #导入math库
r = float(input()) #输入半径值，强转为float类
area = math.pi*r*r #计算面积
print("{:.7f}".format(area)) # 格式化输出，保留小数点后7位


