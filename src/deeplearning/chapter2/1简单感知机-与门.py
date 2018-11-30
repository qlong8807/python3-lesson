#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
• 感知机是具有输入和输出的算法。给定一个输入后，将输出一个既 定的值。
• 感知机将权重和偏置设定为参数。
• 使用感知机可以表示与门和或门等逻辑电路。
• 异或门无法通过单层感知机来表示。
• 使用2层感知机可以表示异或门。
• 单层感知机只能表示线性空间，而多层感知机可以表示非线性空间。
• 多层感知机(在理论上)可以表示计算机。
"""

__author__ = 'Jans'
__date__ = '2018/11/28 17:54'
__createby__ = 'PyCharm'

import numpy as np

# 与门 即&
def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
print('与：')
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

# 与非 &!
def NAND(x1, x2):
    x = np.array([x1, x2])
    # w称为权重，b称为偏置
    w = np.array([-0.5, -0.5]) # 仅权重和偏置与AND不同!
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 或 |
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 仅权重和偏置与AND不同!
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
# 异或  异或门无法通过单层感知机来表示，这里用2层叠加
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y