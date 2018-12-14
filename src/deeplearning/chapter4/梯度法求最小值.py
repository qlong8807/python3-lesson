#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/12/12 14:54'
__createby__ = 'PyCharm'

import sys,os
sys.path.append(os.pardir)
import numpy as np


def numerical_gradient(f,x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # 生成和x形状相同的数组
    for idx in range(x.size):
        tmp_val = x[idx]
        #f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        #f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val #还原值

    return grad

# 梯度下降法
# lr称为超参数。这是一种和神经网络的参数不同的参数。
# 神经网络的参数是通过训练数据和学习算法获得的，而超参数需要人为设定。
# 一般超参数需要尝试多个值，以便学习可以顺利执行。超参数值不同，对结果影响较大。
def gradient_descent(f,init_x,lr=0.01,step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad
    return x

def func2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0,4.0])
res = gradient_descent(func2,init_x,lr=0.1,step_num=100)
print('结果无限接近0')
print(res)