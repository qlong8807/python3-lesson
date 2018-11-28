#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
安装MySQL驱动
pip install mysql-connector-python mysql-connector-python
如果失败请用：pip install mysql-connector

执行INSERT等操作后要调用commit()提交事务；
MySQL的SQL占位符是%s。

"""

__author__ = 'Jans'
__date__ = '2018/1/25 上午9:50'
__createby__ = 'PyCharm'


# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='root1234', database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()