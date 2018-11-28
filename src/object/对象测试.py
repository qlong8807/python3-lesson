#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

class Student(object):
    def __init__(self,name,age):
        self.name = name #这个name外部可以访问
        self.__age = age #两个下划线相当于private

    def set_age(self,age):
        if not isinstance(age, int):
            raise ValueError('age must be an integer!')
        if age < 0 or age > 100:
            raise ValueError('age must between 0 ~ 100!')
        self.__age = age

    def get_age(self):
        return self.__age

    def __str__(self):
        return 'Student object name:%s,age:%s'%(self.name,self.__age)

    __repr__ = __str__


s1 = Student('jans',21)
print(s1.name)
print(s1.get_age())
print(s1)
s1.name = 'lily'
s1.set_age(21)
print(s1.name)
print(s1.get_age())
