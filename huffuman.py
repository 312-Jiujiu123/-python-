# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:53:16 2025

@author: Administrator

number:6

problem:Huffuman树
"""
n = int(input()) #输入一个数n
huffuman = list(map(int,input().split()))#输入map中的值（int）类型，将map中的元素按空格分开，放入list中，该list命名为huffuman
fee = 0 #fee初始化为0，后面用来计算合并节点所需的总的代价
for i in range(n-1):  #遍历huffuman中的权值
#min(huffuman)找到最小的huffuman节点值 huffuman.index(min(huffuman))对应的下标，使用pop方法将该下标位置元素释放huffuman.pop(index)
    temp = huffuman.pop(huffuman.index(min(huffuman))) + huffuman.pop(huffuman.index(min(huffuman)))#把两个最小的取出后q求和，放入temp，序列huffuman中已无两个元素
    huffuman.append(temp)#在huffuman序列中添加刚刚求和的结果
    fee += temp #累加每次计算结果（权重和，总代价）
print(fee)

