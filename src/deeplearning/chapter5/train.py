#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
以TwoLayerNet类为对象，使用MNIST数据集进行学习
"""

__author__ = 'Jans'
__date__ = '2018/12/13 11:16'
__createby__ = 'PyCharm'

import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet


(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True,one_hot_label=True)

#超参数
iters_num = 50000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size/batch_size,1)

for i in range(iters_num):
    # 获取mini-batch
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # grad = network.numerical_gradient(x_batch,t_batch)
    # 通过误差反向传播法计算梯度
    grad = network.gradient(x_batch,t_batch)

    # 更新参数
    for key in ('W1','b1','W2','b2'):
        network.params[key] -= learning_rate * grad[key]

    #记录学习过程
    loss = network.loss(x_batch,t_batch)
    train_loss_list.append(loss)
    if i%iter_per_epoch == 0:
        train_acc = network.accuracy(x_train,t_train)
        test_acc = network.accuracy(x_test,t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(i,train_acc,test_acc)

# 可以发现随着学习的进行，损失函数的值(train_loss_list)在不断减小，表示神经网络的权重参数在逐渐拟合。
