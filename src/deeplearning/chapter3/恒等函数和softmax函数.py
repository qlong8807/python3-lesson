#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
一般而言，回归问题用恒等函数，分类问题用 softmax 函数。

机器学习的问题大致可以分为分类问题和回归问题。
分类问题是数 据属于哪一个类别的问题。
比如，区分图像中的人是男性还是女性 的问题就是分类问题。
而回归问题是根据某个输入预测一个(连续的) 数值的问题。
比如，根据一个人的图像预测这个人的体重的问题就
是回归问题(类似“57.4kg”这样的预测)。

恒等函数会将输入按原样输出，对于输入的信息，不加以任何改动地直 接输出。
"""

__author__ = 'Jans'
__date__ = '2018/11/30 16:57'
__createby__ = 'PyCharm'

import numpy as np


def softmax(a):
    expa = np.exp(a) # 指数函数
    print(expa)
    suma = np.sum(expa)
    print(suma)
    y = expa / suma
    print(y)

a = np.array([0.3, 2.9, 4.0])
softmax(a)

# e的x次方，x如果太大，则会出现内存溢出，提示nan非数字
print('提示非数字')
a = np.array([990,1000,1010])
y = np.exp(a)/np.sum(np.exp(a))
print(y)

# 所以需要修改以上softmax方法，给分子分母都减去一个常数

def softmax2(a):
    c = np.max(a)
    expa = np.exp(a-c) # 溢出策略
    suma = np.sum(expa)
    y = expa/suma
    return y

y = softmax2(a)
print(y)
print('softmax函数求和：',np.sum(y))

'''
softmax 函数的输出是 0.0 到 1.0 之间的实数。
并且，softmax 函数的输出值的总和是 1。
输出总和为 1 是 softmax 函数的一个重要性质。
正 因为有了这个性质，我们才可以把 softmax 函数的输出解释为“概率”。
'''