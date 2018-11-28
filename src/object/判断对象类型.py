#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

print('--------------------type-types-----------------------')
print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
print('-------------------------------------------')
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==str)
print(type('abc')==type(123))
print('-------------------------------------------')

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
print('-------------------------------------------')

print('---------------------isinstance----------------------')
print(isinstance(123,int))
# from 动物对象 import test1
# test1()
import 动物对象
动物对象.test1()
d = 动物对象.Dog()
print(isinstance(d,动物对象.Dog))
print(isinstance(d,动物对象.Animal))
print(isinstance(d,动物对象.Husky))
print(isinstance(d, 动物对象.Dog) and isinstance(d, 动物对象.Animal))
print('---------------------dir 比如，获得一个str对象的所有属性和方法：----------------------')
print(dir('abc'))
print('---------------------调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法----------------------')
print(len('abc'))
print('abc'.__len__())