#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'计算圆周率'

__author__ = 'Jans'

import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    lst = list(range(1,2*N,2))
    sum = 0
    flag = True
    for i in lst:
        if flag :
            temp = sum;
            sum += 4/i
            print(str(temp)+"  +  "+str(4/i) + "  =  "+str(sum))
            flag = False
        else :
            temp = sum;
            sum -= 4/i
            print(str(temp)+"  -  "+str(4/i) + "  =  "+str(sum))
            flag = True
    return sum


if __name__ == '__main__':
    print(pi(1000000))