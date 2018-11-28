#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
当前文档注释
"""

__author__ = 'Jans'
__date__ = '2018/7/20 15:32'
__createby__ = 'PyCharm'

import md5
import sys


class Encoder(object):
    def encode_64(self, input_str):
        md5_obj = md5.new()
        md5_obj.update(input_str)
        md5hex = md5_obj.digest()
        md5sum0 = (ord(md5hex[3]) << 24) | (ord(md5hex[2]) << 16) \
                  | (ord(md5hex[1]) << 8) | ord(md5hex[0])
        md5sum1 = (ord(md5hex[7]) << 24) | (ord(md5hex[6]) << 16) \
                  | (ord(md5hex[5]) << 8) | ord(md5hex[4])
        md5sum2 = (ord(md5hex[11]) << 24) | (ord(md5hex[10]) << 16) \
                  | (ord(md5hex[9]) << 8) | ord(md5hex[8])
        md5sum3 = (ord(md5hex[15]) << 24) | (ord(md5hex[14]) << 16) \
                  | (ord(md5hex[13]) << 8) | ord(md5hex[12])
        sign1 = (md5sum0 + md5sum2) & 0xffffffff
        sign2 = (md5sum1 + md5sum3) & 0x7fffffff
        result = (sign1 | (sign2 << 32))
        return str(result)


if __name__ == '__main__':
    # a = '0403FCA3FB4EDF022F179D9B48B79674'
    # result = encoder.encode_64(a)
    encoder = Encoder()
    for line in sys.stdin:
        linelist = line.strip().split('\t')
        cuid = linelist[0]
        result = encoder.encode_64(cuid)
        print('%s\t%s' % (result, cuid))