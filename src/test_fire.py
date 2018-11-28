#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
pip3 intall fire
可以在命令行中输入以下命令查看输出
python test_fire.py
python test_fire.py 20180101 20180309
"""

__author__ = 'Jans'
__date__ = '2018/3/27 下午4:08'
__createby__ = 'PyCharm'


import fire
import datetime

def cal_days(date1,date2):
    '''计算两个日期之间的天数'''
    date1_str = str(date1)
    date2_str = str(date2)
    d1 = datetime.datetime.strptime(date1_str,'%Y%m%d')
    d2 = datetime.datetime.strptime(date2_str,'%Y%m%d')
    dn = d2-d1
    return dn.days

if __name__ == '__main__':
    fire.Fire(cal_days)