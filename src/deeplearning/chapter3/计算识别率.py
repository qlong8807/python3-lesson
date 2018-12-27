#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
根据已经学习好的参数，计算测试数据的识别率
"""

__author__ = 'Jans'
__date__ = '2018-12-14 16:15'
__createby__ = 'PyCharm'

import sys,os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import numpy as np
import pickle

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def get_data():
    (x_train,t_train),(x_test,t_test) = load_mnist(flatten=True,normalize=False)
    return x_test,t_test

# sample_weight.pkl文件中保存了学习到的权重参数和偏置
def init_network():
    with open("sample_weight.pkl",'rb') as f:
        network = pickle.load(f)
    return network

# 通过权重和偏置，计算，返回识别出的概率数组
def predict(network,x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']
    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = softmax(a3)
    return y

x,t = get_data()
network = init_network()
# 识别精度
accurary_cnt = 0
print('xlen:',len(x))
tw3 = network['W3']
print(tw3.shape)
for i in range(len(x)):
    y = predict(network,x[i])
    p = np.argmax(y) # 获取概率最高的元素的索引
    if(i < 10):
        print('识别概率数组：',y)
        print('数组中最大值的索引',p)
    if p == t[i]:
        accurary_cnt += 1

print("识别精度:"+str(float(accurary_cnt)/len(x)))