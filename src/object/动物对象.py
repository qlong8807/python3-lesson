#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

class Animal(object):#继承自object
    def run(self):
        print('animal is running')

class Dog(Animal):#继承自Animal
    def run(self):#重写run方法
        print('dog is running')


class Husky(Dog):
    def run(self):
        print('husky is running')

def test1():
    print('动物对象中的test1方法')