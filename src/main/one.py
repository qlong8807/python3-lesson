#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

print('one 开始执行')
print(__name__)

def func():
    print('one func() 被执行了')


if __name__ == "__main__":
    print("one.py 直接运行自己")
else:
    print("one.py 是导入后被执行的")

