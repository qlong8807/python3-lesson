#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

import requests
import json
import math


def get_sup_info(url, page):
    params = {
        'ajaxtype': 1,
        'page': page,
        'category': 1,
        'pageSize': 8
    }
    cookies = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Cookie': 'acw_tc=AQAAAKLQ3U/WTAYAggq7PZ24WOlm9vQW; PHPSESSID=r0nbvk7hppjftegk4fpt9cu535; _uab_collina=150094753858198811653567; mdswv=v1.0; mdsa=MD-STICS-5976a44746eca; mdss=6-o; mdsf=md; mdsff=www_so_com; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22caefb4c752d5877e1c5aa4aa5df37e99%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22123.57.117.133%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A109%3A%22Mozilla%2F5.0+%28Windows+NT+6.1%3B+WOW64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F57.0.2987.133+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1500949741%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D688590410f74ae5570846b68edaa6a67; u_asec=090%23qCQXOTXPXpnXuvi0XXXXXuS8vzgEjU05DQJMOF5UA9EUDzQmhY5%2BGl8VXvXQMcYTnuxiXXf8AfIwSTQXU6hnXXa3HoQCh9T4gY73OjjeG%2FXUHYVms%2BhnDXG3Hoqhh9kvan73O51TXvXuLWQ5Hfv5oTQXaOXTs7%2BZhPNGlTQXFdOVReD%2FItB4na8Dnin5Lm97WiM5ra4hxeC7S3lO6usAcNvwY4vCdr7HxBzviaxEIhQGz7LKItio9zCD7XwC65ZVdC6hXZCHFeYVapLaISEbstnWekYGxg9lzXcEX5lZOhntBpwW6glEhtlW9kNvXvXKxprV%2B%2FSVO5OeHhobpDlHgCz6CITLvzBvaOviXXFKMieaRAn%3D; SERVERID=75c0ee4e77ef78c56ac6e5a297fdd0b8|1500949742|1500947526'
    }
    html = requests.post(url, data=params, headers=cookies)
    json_data = json.loads(html.text)
    des = json_data['des']
    for data in des:
        name = data['name']
        id = data['id']
        pay_count = data['pay_count']
        all_page = math.ceil(int(pay_count) / 20)
        for i in range(1, int(all_page) + 1):
            get_app_info(i, id, name)


def get_app_info(page, id, name):
    params = {
        'pro_id': id,
        'type': '1',
        'page': page,
        'pageSize': '20'
    }
    cookies = {
        'User-Agent': 'xx',
        'Cookie': 'xx'
    }
    html = requests.post('https://wds.modian.com/ajax_backer_list', data=params, headers=cookies)
    json_data = json.loads(html.text)
    datas = json_data['data']
    for data in datas:
        nickname = data['nickname']
        money = data['total_back_amount']
        print(name, nickname, money)


if __name__ == '__main__':
    for i in range(1, 10):
        get_sup_info('https://wds.modian.com/ajax_first', i)