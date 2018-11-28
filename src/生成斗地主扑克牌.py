# coding:utf8
# author:jans
# desc: 扑克牌洗牌

import random

poker_num = [str(i) for i in range(2,11)]
poker_str = ['A','J','Q','K']
poker_king = ['大王','小王']

poker_color = ['红','黑','方','花']

pokers = ['%s%s' %(i,j) for i in poker_color for j in poker_num+poker_str] + poker_king

print(len(pokers))
print(pokers)

print('开始洗牌')
random.shuffle(pokers)
print('洗牌中。。。')
print(pokers)

#斗地主发牌
person_a = pokers[0:51:3]
person_b = pokers[1:51:3]
person_c = pokers[2:51:3]
last_3 = pokers[-3:]
print('第一个人的牌：',person_a)
print('第二个人的牌：',person_b)
print('第三个人的牌：',person_c)
print('底牌：',last_3)