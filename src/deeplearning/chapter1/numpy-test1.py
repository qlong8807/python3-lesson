#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
数组和矩阵
"""

__author__ = 'Jans'
__date__ = '2018/11/29 14:48'
__createby__ = 'PyCharm'


import numpy as np

x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])

print(x+y)
print(x*y)
print(x-y)
# 广播
print(x/2)

print('numpy多维数组')

x = np.array([[1,2],[3,4]])
print('数组x:',x)
print('维数：',np.ndim(x))
print("形状:",x.shape)
print("数据类型:",x.dtype)
print(type(x.shape))
y = np.array([[0,3],[2,3]])

print(x*y)
#广播
print('广播')
print(x*3)
z=np.array([2,5])
print(x*z)
print(x-z)

print('转为一维数组')
print(x.flatten())
print('获取满足一定条件的数组元素')
print(x[x>1])