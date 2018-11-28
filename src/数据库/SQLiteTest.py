#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
"""

__author__ = 'Jans'

#导入驱动
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
#创建一个Cursor
cursor = conn.cursor()
cursor.execute('drop table if exists user')
#执行SQL，创建User表
cursor.execute('create table user(id varchar(32) primary key,name varchar(32),age int)')
cursor.execute('insert into user values("1","张三",21)')
cursor.execute('insert into user values("2","李四",22)')
#获得影响的行数
c = cursor.rowcount
print(c)
#查询
# cursor.execute('select * from user where id = ?',('1',))
cursor.execute('select * from user')
# 获取第一行数据
row_1 = cursor.fetchone()
print(row_1)
# 获取前n行数据
row_2 = cursor.fetchmany(3)
print(row_2)
# 获取所有数据
row_3 = cursor.fetchall()
print(row_3)
#关闭Cursor
cursor.close()
conn.commit()
conn.close()