#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
MNIST数据为28*28像素的图片
训练数据60000张
测试数据10000张
"""

__author__ = 'Jans'
__date__ = '2018-12-13 15:41'
__createby__ = 'PyCharm'


import sys,os
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
import numpy as np
# 第1个参数normalize设置是否将输入图像正规化为0.0--1.0的值，FALSE则会保持为0--255
# 第2个参数flatten设置是否展开输入图像。True则返回784个元素构成的一维数组，False返回1*28*28的三维数组
# 第3个参数one_hot_label设置是否将标签保存为one-hot表示。
(x_train,t_train),(x_test,t_test) = load_mnist(flatten=True,normalize=False)

# 输出各个数据的形状
print('x_train:',x_train.shape)
print('t_train:',t_train.shape)
print('x_test:',x_test.shape)
print('t_test',t_test.shape)

print(t_train[0])
# print(x_train[0].dtype)
print(np.max(x_train[0]))
print(np.where(np.max(x_train[0])))
# print(x_train[0])
