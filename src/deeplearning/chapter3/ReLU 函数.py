#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
ReLU 函数在输入大于 0 时，直接输出该值;在输入小于等于 0 时，输 出 0
"""

__author__ = 'Jans'
__date__ = '2018/11/29 17:10'
__createby__ = 'PyCharm'

import numpy as np
import matplotlib.pylab as plt


# 之所以 sigmoid 函数的实现能支持 NumPy 数组，秘密就在于 NumPy 的 广播功能
def relu(x):
    return np.maximum(0,x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
# plt.ylim(-0.1,1.1) # 指定y轴范围
plt.show()
