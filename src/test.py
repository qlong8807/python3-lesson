#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/5/2 上午8:57'
__createby__ = 'PyCharm'

class A:
    def foo(self,x):
        print('foo:',x)

    @classmethod
    def class_foo(cls,x):
        print('class_foo:',x)

    @staticmethod
    def static_foo(x):
        print('static foo:',x)
a = A()
a.foo(1)
A.foo(a,2)

a.class_foo(3)
A.class_foo(4)

a.static_foo(5)
A.static_foo(6)