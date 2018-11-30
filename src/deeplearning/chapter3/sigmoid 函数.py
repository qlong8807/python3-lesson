#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
h(x) = 1 / (1  + exp(-x))
 exp(−x) 表示 e(−x) 的意思
 e 是纳皮尔常数 2.7182 . . .
"""

__author__ = 'Jans'
__date__ = '2018/11/29 17:10'
__createby__ = 'PyCharm'

import numpy as np
import matplotlib.pylab as plt


# 之所以 sigmoid 函数的实现能支持 NumPy 数组，秘密就在于 NumPy 的 广播功能
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
# plt.ylim(-0.1,1.1) # 指定y轴范围
plt.show()
