#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
3层神经网络
这 里 定 义 了 init_network() 和 forward() 函 数。init_network() 函 数 会 进
行权重和偏置的初始化，并将它们保存在字典变量 network 中。这个字典变 量 n e t w o r k
中 保 存 了 每 一 层 所 需 的 参 数 ( 权 重 和 偏 置 )。 f o r w a r d ( ) 函 数
中 则 封 装了将输入信号转换为输出信号的处理过程。
"""

__author__ = 'Jans'
__date__ = '2018/11/30 16:51'
__createby__ = 'PyCharm'

import numpy as np


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y

def identity_function(x):
    return x
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # [ 0.31682708 0.69627909]