#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
运行后会把新浪的首页保存到当前文件夹下
"""

__author__ = 'Jans'
__date__ = '2018/1/25 下午4:12'
__createby__ = 'PyCharm'


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()