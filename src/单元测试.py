#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

import unittest


class Test1(unittest.TestCase):
    def test_method1(self):
        v1 = 1
        self.assertEqual(v1, 1)
        self.assertTrue(1, 1)
        print('exe finish')

    def setUp(self):  # 测试执行前调用该方法
        print('setup')

    def tearDown(self):  # 测试执行完调用该方法
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
