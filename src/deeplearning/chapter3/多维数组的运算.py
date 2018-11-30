#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/11/30 09:22'
__createby__ = 'PyCharm'


import numpy as np

A = np.array([[2,3],[4,5]])

B = np.array([[3,2],[6,5]])

print('多维数组2*2  2*2相乘，行✖️列：')
print(np.dot(A,B))

C = np.array([3])
print('多维数组2*2  1相乘，行✖️列：')
# print(np.dot(A,C))

C = np.array([3,6])
print('多维数组2*2  1*2相乘，行✖️列：')
print(np.dot(A,C))

D = np.array([[3],[8]])
print('多维数组2*2  2*1相乘，行✖️列：')
print(np.dot(A,D))
