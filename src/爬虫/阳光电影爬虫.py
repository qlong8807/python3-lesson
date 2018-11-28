#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

import requests
import re
from lxml import etree
import csv


def get_cate_info(url):
    res = requests.get(url)
    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    infos = html.xpath('//div[@class="contain"]/ul/li[position()<12]')
    for info in infos:
        cate_name = info.xpath('a/text()')[0]
        cate_url = res.url + info.xpath('a/@href')[0]
        get_movie(cate_url, cate_name)
        # print(cate_name,cate_url)


def get_movie(url, cate_name):
    res = requests.get(url)
    res.encoding = 'gb2312'
    all_page = re.findall('共(.*?)页', res.text)
    kind = re.findall('<option value=\'(list_.*?_).*?', res.text)
    if len(all_page) > 0:
        kind_url = url.rstrip(url.split('/')[-1]) + str(kind[0])
        for page in range(1, int(all_page[0]) + 1):
            page_url = kind_url + str(page) + '.html'
            resp = requests.get(page_url)
            resp.encoding = 'gb2312'
            html = etree.HTML(resp.text)
            infos = html.xpath('//div[@class="co_content8"]/ul//table')
            for info in infos:
                detail_url = 'http://www.ygdy8.com' + info.xpath('tr[2]/td[2]/b/a/@href')[0]
                movie_name = info.xpath('tr[2]/td[2]/b/a/text()')[0]
                print(detail_url)
                get_resource(detail_url, cate_name, url, movie_name)
            # print(page_url)


def get_resource(url, cate_name, cate_url, movie_name):
    res = requests.get(url)
    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    movie_resource = html.xpath('//tbody//tr/td/a/text()')[0]
    writer.writerow((cate_name, cate_url, movie_name, url, movie_resource))
    print(movie_resource)


if __name__ == '__main__':
    fp = open(r'C:\Users\Public\Desktop\dianyin.csv', 'w+', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('cate_name', 'cate_url', 'movie_name', 'movie_url', 'movie_resource'))

    get_cate_info('http://www.ygdy8.com/')