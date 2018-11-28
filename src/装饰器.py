#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'打印函数执行时间'

__author__ = 'Jans'

import functools,time


def exetime(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        begin=time.time()
        fv=fn(*args,**kw)
        end=time.time()
        print('%s executed in %s s' % (fn.__name__,end-begin))
        return fv
    return wrapper


@exetime
def fun1():
    print('start exe fun1')
    time.sleep(1)
    print('end exe fun1')


if __name__ == '__main__':
    fun1()