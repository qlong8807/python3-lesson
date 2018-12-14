#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
以TwoLayerNet类为对象，使用MNIST数据集进行学习
"""

__author__ = 'Jans'
__date__ = '2018/12/13 11:16'
__createby__ = 'PyCharm'

import numpy as np
from dataset.mnist import load_mnist
from TwoLayerNet import TwoLayerNet


(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True,one_hot_label=True)

train_loss_list = []
print('111')
#超参数
iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
print('222')
for i in range(iters_num):
    # 获取mini-batch
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print("i=",i)
    # 计算梯度
    grad = network.numerical_gradient(x_batch,t_batch)
    #grad = network.gradient(x_batch,t_batch)

    # 更新参数
    for key in ('W1','b1','W2','b2'):
        network.params[key] -= learning_rate * grad[key]

    #记录学习过程
    loss = network.loss(x_batch,t_batch)
    train_loss_list.append(loss)

# 可以发现随着学习的进行，损失函数的值(train_loss_list)在不断减小，表示神经网络的权重参数在逐渐拟合。
print("----------")
print(train_loss_list.__len__())