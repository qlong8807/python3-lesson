#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
x>0 return 1;
x<=0 return 0;
这就是阶跃函数
"""

__author__ = 'Jans'
__date__ = '2018/11/29 17:10'
__createby__ = 'PyCharm'

import numpy as np
import matplotlib.pylab as plt


# 阶跃函数
def step_func(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_func(x)
plt.plot(x, y)
# plt.ylim(-0.1,1.1) # 指定y轴范围
plt.show()
