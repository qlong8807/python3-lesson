#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

class Student(object):
    name = 'Stu'


s1 = Student()
s2 = Student()

print(s1.name)
print(s2.name)
print(Student.name)
print("-------------------------")
s1.name = 'machel'
print(s1.name)
print(s2.name)
print(Student.name)
print("-------------------------")
del s1.name
print(s1.name)
print(s2.name)
print(Student.name)

