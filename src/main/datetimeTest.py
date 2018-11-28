#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

from datetime import datetime
#获取当前时间
print(datetime.now())

dt1 = datetime(2015,12,11,18,30,15)
print(dt1)

t = dt1.timestamp()
print(t)

print(datetime.fromtimestamp(t)) #本地时间
print(datetime.utcfromtimestamp(t)) #UTC时间

st = '2018-01-11 14:55:01'
print(datetime.strptime(st,'%Y-%m-%d %H:%M:%S'))