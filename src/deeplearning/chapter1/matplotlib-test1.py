#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/11/29 15:15'
__createby__ = 'PyCharm'


import numpy as np
import matplotlib.pyplot as plt

#生成数据
x = np.arange(0,6,0.1)
y = np.sin(x)
print('X= ',x)

#绘制图形

plt.plot(x,y)
plt.show()