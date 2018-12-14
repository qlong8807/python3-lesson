#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/12/13 10:27'
__createby__ = 'PyCharm'


import sys,os
sys.path.append(os.pardir)
from common.functions import *
from common.gradient import numerical_gradient

class TwoLayerNet:
    # 输入层神经元数、隐藏层神经元数、输出层神经元数
    def __init__(self,input_size,hidden_size,output_size,weight_init_std=0.01):
        # 初始化权重
        # params保存神经网络的参数的字典型变量，W1是第一层的权重，b1是第一层的偏置，W2是第2层的权重，b2是第2层的偏置
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size,hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size,output_size)
        self.params['b2'] = np.zeros(output_size)

    # 进行识别（推理）。x是图像数据
    def predict(self,x):
        W1,W2 = self.params['W1'],self.params['W2']
        b1,b2 = self.params['b1'],self.params['b2']
        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1,W2) + b2
        y = softmax(a2)
        return y

    # 计算损失函数的值。x :输入的图像数据，t:监督数据（正确解标签）
    # 该方法会基于predict()的结果和正确解标签，计算交叉熵误差。
    def loss(self,x,t):
        y = self.predict(x)
        return cross_entropy_error(y,t)
    # 计算识别精度
    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        t = np.argmax(t,axis=1)
        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy

    # 计算权重参数的梯度。x :输入的图像数据，t:监督数据（正确解标签）
    # 基于数值微分计算参数的梯度，速度较慢
    def numerical_gradient(self,x,t):
        loss_W = lambda W:self.loss(x,t)
        # grads保存梯度的字典型变量，W1是第一层的权重，b1是第一层的偏置，W2是第2层的权重，b2是第2层的偏置
        grads = {}
        grads['W1'] = numerical_gradient(loss_W,self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W,self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W,self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W,self.params['b2'])
        return grads

    #计算权重参数的梯度。numerical_gradient的高速版
    # 基于误差反向传播法计算参数的梯度，速度较快
    def gradient(self,x,t):
        return x


net = TwoLayerNet(input_size=784,hidden_size=100,output_size=10)
print(net.params['W1'].shape)
print(net.params['W2'].shape)
print(net.params['b1'].shape)
print(net.params['b2'].shape)