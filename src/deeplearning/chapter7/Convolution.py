#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018-12-27 09:54'
__createby__ = 'PyCharm'

import numpy as np
from common.util import im2col


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        FN, C, FH, FW = self.W.shape #滤波器是(FN, C, FH, FW)的4维形状。
        N, C, H, W = x.shape
        out_h = int(1 + (H + 2 * self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2 * self.pad - FW) / self.stride)

        col = im2col(x,FH,FW,self.stride,self.pad) # 参数：数据，滤波器的高，滤波器的长，步幅，填充
        col_W = self.W.reshape(FN,-1).T #滤波器的展开
        out = np.dot(col,col_W) + self.b

        out = out.reshape(N,out_h,out_w,-1).transpose(0,3,1,2)
        #transpose会更改多维数组的轴的顺序。上面的是把(N,H,W,C)改为(N,C,H,W)
        return out
