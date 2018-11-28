#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

import requests
import time
import json
from datetime import datetime
from subprocess import call

# 苏州SZH,西安XAY,南京NJH
station_suzhou = 'SZH'  # 苏州
station_xian = 'XAY'  # 西安
station_huashan = 'HSY'  # 华山
station_shanghai = 'SHH'  # 上海
station_ningqiang = 'NOY'  # 宁强南
station_nanjing = 'NJH'  # 南京
station_weinan = 'WNY'  # 渭南
station_tongguan = 'TGY'  #潼关
# 是否需要无座
need_wuzuo = False


# 是否是数字
def is_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
# 是否有票
def has_ticket(s):
    if '无' != s and '' != s:
        return True
    else:
        return False

# 查询和打印，checis为车次的数组或者字符串*,patten_str为车次开头的字符，没有就不用输入
def queryAndPrint(train_date, start_station, end_station, checis, pattern_str=''):
    # print('data:' + train_date + ',start:' + start_station + ',end:' + end_station + ',checi:' + str(
    #     checis) + ',patten:' + patten_str)
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + train_date + '&leftTicketDTO.from_station=' + start_station + '&leftTicketDTO.to_station=' + end_station + '&purpose_codes=ADULT'
    headerstr = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    cookiesstr = {'token': '12345', 'status': 'working'}
    try:
        r = requests.get(url, headers=headerstr, cookies=cookiesstr, timeout=3.5)  # 3.5秒后超时
        # print('响应状态码：' + str(r.status_code) + '，编码：' + str(r.encoding))
        # content = r.content.decode()
        # print('返回内容是：' + content)
        piao_infos = r.json().get('data').get('result')
    except requests.exceptions.ReadTimeout:
        print('ReadTimeout：' + url)
        return None
    except requests.exceptions.ConnectionError:
        print('ConnectionError：' + url)
        return None
    except json.decoder.JSONDecodeError:
        print('请求到的json解析错误：%s' % r.content)
        return None
    # print(type(piao_infos))
    # print('车票信息：' + str(piao_infos))
    # print('车票信息：'+ piao_infos[0])
    for i in piao_infos:
        # i就是1列车次的字符串格式信息
        piao_info = i.split('|')
        current_train_no = piao_info[3]
        if '*' == checis:
            if current_train_no.startswith(pattern_str):
                checi = piao_info[3]
                wopu = piao_info[-9]
                yingzuo = piao_info[-8]
                zuowei_level2 = piao_info[-7]
                wuzuo = piao_info[-11]
                zuowei_level1 = piao_info[-6]
                # print('车次：'+current_train_no+',一等座：'+zuowei_level1+',二等座：'+zuowei_level2)
                if has_ticket(wopu) or has_ticket(yingzuo) or (need_wuzuo & has_ticket(wuzuo)) or has_ticket(zuowei_level2):
                    print('赶快订票---》》》日期:' + train_date + ',从:' + start_station + ',到:' + end_station +
                          ',车次：' + checi + ',一等座：' + zuowei_level1 + ',二等座：' + zuowei_level2 + ',卧铺：' + wopu + ',硬座：' + yingzuo + ',无座：' + wuzuo)
                    cmd = 'display notification \"' + '日期:' + train_date + ',从:' + start_station + ',到:' + end_station + \
                          ',车次:' + checi + ',一等座：' + zuowei_level1 + ',二等座：' + zuowei_level2 + ',卧铺:' + wopu + ',硬座:' + yingzuo + ',无座:' + wuzuo + '。\" with title \"赶快订票\"'
                    call(["osascript", "-e", cmd])
        elif current_train_no in checis:
            checi = piao_info[3]
            wopu = piao_info[-9]
            yingzuo = piao_info[-8]
            zuowei_level2 = piao_info[-7]
            wuzuo = piao_info[-11]
            if has_ticket(wopu) or has_ticket(yingzuo) or (need_wuzuo & has_ticket(wuzuo)) or has_ticket(zuowei_level2):
                print('赶快订票---》》》日期:' + train_date + ',从:' + start_station + ',到:' + end_station +
                      ',车次：' + checi + ',二等座：' + zuowei_level2 + ',卧铺：' + wopu + ',硬座：' + yingzuo + ',无座：' + wuzuo)
                cmd = 'display notification \"' + '日期:' + train_date + ',从:' + start_station + ',到:' + end_station + \
                      ',车次:' + checi + ',二等座：' + zuowei_level2 + ',卧铺:' + wopu + ',硬座:' + yingzuo + ',无座:' + wuzuo + '。\" with title \"赶快订票\"'
                call(["osascript", "-e", cmd])
        else:
            pass
    print(str(datetime.now()) + "没有查询到" + train_date + "从《" + start_station + "》到《" + end_station + "》的车次《" + str(
        checis) + "》的票" + ('' if '' == pattern_str else ", 前正则：" + pattern_str))


if __name__ == '__main__':
    time1 = datetime.now()
    cmd = 'display notification \"' + \
          '车票查询开始运行。\" with title \"订票程序\"'
    call(["osascript", "-e", cmd])
    # 循环查询车票信息except (AssertionError,ZeroDivisionError),arg:
    while True:
        # queryAndPrint('2018-02-23', station_huashan, station_suzhou, ['D308','G4324','G1976'])
        # queryAndPrint('2018-02-23', station_xian, station_shanghai, ['D308','G4324','G1976'])
        # queryAndPrint('2018-02-23', station_huashan, station_shanghai, ['D308','G4324','G1976'])
        # queryAndPrint('2018-02-24', station_huashan, station_suzhou, ['D308','G4324','G1976'])
        # queryAndPrint('2018-02-24', station_xian, station_shanghai, ['D308','G4324','G1976'])
        # queryAndPrint('2018-02-24', station_huashan, station_shanghai, ['D308','G4324','G1976'])
        # queryAndPrint('2018-02-11', station_suzhou, station_huashan, ['Z252'])
        # queryAndPrint('2018-02-11', station_suzhou, station_xian, ['Z252'])
        # queryAndPrint('2018-02-11', station_shanghai, station_huashan, ['Z252'])
        # queryAndPrint('2018-02-11', station_shanghai, station_xian, ['Z252'])
        queryAndPrint('2018-02-28', station_xian, station_suzhou, '*', 'Z')
        queryAndPrint('2018-02-28', station_xian, station_suzhou, '*', 'T')
        # queryAndPrint('2018-03-01', station_xian, station_suzhou, '*', 'Z')
        # queryAndPrint('2018-03-02', station_xian, station_suzhou, '*', 'Z')
        # queryAndPrint('2018-03-03', station_xian, station_suzhou, '*', 'Z')
        # queryAndPrint('2018-03-04', station_xian, station_suzhou, '*', 'Z')
        # queryAndPrint('2018-03-05', station_xian, station_suzhou, '*', 'Z')
        # queryAndPrint('2018-02-24', station_xian, station_shanghai, ['Z94','Z88','Z166','Z42','Z254','Z218'])
        time2 = datetime.now()
        between_time = (time2 - time1).seconds
        if between_time > 300:
            cmd = 'display notification \"' + \
                  '车票查询正在运行中。\" with title \"订票程序\"'
            call(["osascript", "-e", cmd])
            time1 = datetime.now()
        time.sleep(1)
