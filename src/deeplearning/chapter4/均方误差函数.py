#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/12/12 14:34'
__createby__ = 'PyCharm'

import numpy as np

# y表示神经网络的输出，t表示监督数据
def mean_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2)
#  “2”为正 解
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

#  1:“2”的概  高的   0.6
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
r1 = mean_squared_error(np.array(y), np.array(t))
print(r1)

#  2:“7”的概  高的   0.6
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
r2 = mean_squared_error(np.array(y), np.array(t))
print(r2)

# 第一个例子中，正解是“2”，神经网络的最大输出的是“2”
# 第二个例子中，正解是“2”，神经网络的最大输出的是“7”。
# 如实验结果所示，我们发现第一个例子的损失函数的值更小，和监督数据直接的误差较小。
# 也就是说，均方误差显示第一个例子的输出结果和监督数据更加吻合。