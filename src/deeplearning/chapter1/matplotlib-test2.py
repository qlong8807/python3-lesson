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
y1 = np.sin(x)
y2 = np.cos(x)

#绘制图形

plt.plot(x,y1,label='sin')
plt.plot(x,y2,linestyle='--',label='cos') # 这里虚线值能用2个-，不能用多个
# plt.plot(x, y2, linestyle = "--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos2')
plt.legend()
plt.show()