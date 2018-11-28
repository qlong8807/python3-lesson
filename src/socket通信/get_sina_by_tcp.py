#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
运行后会把新浪的首页保存到当前文件夹下
"""

__author__ = 'Jans'
__date__ = '2018/1/25 下午4:12'
__createby__ = 'PyCharm'


import socket

#创建一个socket，AF_INET为IPV4
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)
# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)