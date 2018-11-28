# coding:utf8
# author:jans
# desc:彩票号码
# 35选5，12选2 7

import random

daletou_qian = [i for i in range(1,36)]
daletou_hou = [i for i in range(1,13)]

qian_random = random.sample(daletou_qian,k=5)
hou_random = random.sample(daletou_hou,k=2)

print(qian_random+hou_random)