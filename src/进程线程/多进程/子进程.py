#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/1/25 下午5:20'
__createby__ = 'PyCharm'


import subprocess

# 如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
# 如果子进程还需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''
上面的代码相当于在命令行执行命令nslookup，然后手动输入：
set q=mx
python.org
exit

'''