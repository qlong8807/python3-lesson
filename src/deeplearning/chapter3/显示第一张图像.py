#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
显示第一张MNIST数据集中的图片
"""

__author__ = 'Jans'
__date__ = '2018-12-13 17:03'
__createby__ = 'PyCharm'


import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train,t_train),(x_test,t_test) = load_mnist(flatten=True,normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28,28) # 把图像的形状变成原来的尺寸
print(img.shape)

img_show(img)