#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
"""

__author__ = 'Jans'
__date__ = '2018/1/25 下午4:20'
__createby__ = 'PyCharm'


import socket,time,threading

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 监听端口
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
# 不需要调用listen()方法，而是直接接收来自任何客户端的数据
while True:
    # 接收数据: recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)