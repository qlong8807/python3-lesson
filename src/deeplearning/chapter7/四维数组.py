#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
CNN中各层间传递的数据是4维数据
比如：数据的形状是(10,1,28,28)
    对应10个高长为28、通道数为1的数据

CNN中会把4维数据展开为2维，进行计算后，再把2维合并为4维
"""

__author__ = 'Jans'
__date__ = '2018-12-26 17:44'
__createby__ = 'PyCharm'


import numpy as np

x = np.random.rand(10,1,28,28) # 随机生成数据

print(x.shape)

print('x[0]的形状：',x[0].shape)

print('x[0,0]的形状',x[0,0].shape)


import sys,os
sys.path.append(os.pardir)
from common.util import im2col

x1 = np.random.rand(1,3,7,7)
col1 = im2col(x1,5,5,stride=1,pad=0) # 参数：数据，滤波器的高，滤波器的长，步幅，填充
print(col1.shape)
# 第二维的值为3*5*5

x2 = np.random.rand(10,3,5,5)
print('测试reshape:',x2.reshape(10,-1).shape)
col2 = im2col(x2,3,3,stride=1,pad=0)
print(col2.shape)
# 第二维的值为3*3*3