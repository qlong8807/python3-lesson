#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
激活函数的正向传播、反向传播的实现

神经网络正向传播的流程：x,w,b是输入、权重、偏置，经过y = np.dot(x,w)+b,
然后y经过激活函数的转换后，传递到下一层。

矩阵的乘积：
X * W = O
(2,)*(2,3)=(3,)
"""

__author__ = 'Jans'
__date__ = '2018-12-21 14:46'
__createby__ = 'PyCharm'

import numpy as np


class Relu:
    '''
    relu函数即 y = np.maximum(0,x)
    Relu层就像电路中的开关，正向传播时，有电流流过就把开关设为ON，没电流流过就把开关设为OFF；
    反向传播时，开关为ON，电流就会流过，开关为OFF电流就不会流过
    '''
    def __init__(self):
        ''' mask是由True/False组成的 NumPy数组'''
        self.mask = None

    def forward(self,x):
        '''正向传播'''
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self,dout):
        '''逆向传播'''
        dout[self.mask] = 0
        dx = dout
        return dx

print('测试：')
x = np.array([[1,-2,4],[0,3,5],[-5,2,-1]])
relu = Relu()
print(relu.forward(x))
# print('backward:',relu.backward(1))

class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self,x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self,dout):
        dx = dout * (1 - self.out) * self.out
        return dx

print('测试sigmoid:')
x = np.arange(-5.0, 5.0, 0.1)
sig = Sigmoid()
print(sig.forward(x))
print('backward:',sig.backward(1))

class Affine:
    '''
    y = (x * W) + B
    '''
    def __init__(self,W,B):
        self.W = W
        self.B = B
        self.x = None
        self.dW = None
        self.dB = None

    def forward(self,x):
        self.x = x
        out = np.dot(x,self.W) + self.B
        return out

    def backward(self,dout):
        dx = np.dot(dout,self.W.T)
        self.dW = np.dot(self.x.T,dout)
        self.dB = np.sum(dout,axis=0)
        return dx


def softmax(a):
    c = np.max(a)
    expa = np.exp(a - c)  # 溢出策略
    suma = np.sum(expa)
    y = expa / suma
    return y

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size



class Softmax:
    '''
    将输出进行正规化，即输出的和为1.
    神经网络中进行的处理有推理和学习，
    推理是一般使用softmax层前一层作为识别结果（得分）,因为这时只选取最大值；
    学习阶段需要使用softmax函数计算比例。

    这里的实现也包含作为损失函数的交叉熵误差，所以被称为softmax-with-loss层。
    '''
    def __init__(self):
        self.loss = None # 损失
        self.y = None # softmax的输出
        self.t = None # 监督数据(one-hot vector)


    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y,self.t)
        return self.loss
    def backward(self,dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx



