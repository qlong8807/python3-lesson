#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/5/2 上午8:57'
__createby__ = 'PyCharm'


num = (lambda a,b,c:b**2-4*a*c)(3,4,2)
print(num)

print('9*9乘法表')

for i in range(1,10):
    for j in range(i,10):
        print("{} * {} = {}".format(i,j,i*j),end="\t")
    print()