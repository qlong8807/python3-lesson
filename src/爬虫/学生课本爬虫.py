#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'从教育网站，爬取中小学教材PDF文件地址，然后下载到本地'

__author__ = 'Jans'

import requests
from bs4 import BeautifulSoup
import os

base_path = 'D:\\zyl\\人教版中小学教材' # 教材保存的本地目录
http_pre_path = 'https://bp.pep.com.cn/jc/' # 教材网站


def crawl(url):
    # 请求首页html
    # response = requests.get(url,timeout=5)
    # response.encoding = response.apparent_encoding
    # soup = BeautifulSoup(response.text,'html5lib')
    # with open('D:\\zyl\\python3-lesson\\book-home.html', 'r', encoding='UTF-8') as f:
    #     print(f.read())
    html_str = open('D:\\zyl\\python3-lesson\\book-home.html', "r", encoding='UTF-8')
    # 构建soup对象
    soup = BeautifulSoup(html_str, 'html5lib')
    index_a = 1 # 文件夹序号
    for tab in soup.find_all("div", 'list_sjzl_jcdzs2020'):# 循环不通类别的书籍，小学、初中...
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        top_path = base_path + "\\" + str(index_a) +". "+tab.h5.text
        index_a = index_a + 1
        if not os.path.exists(top_path): # 如果当前类别文件夹不存在，则创建
            os.mkdir(top_path)
        print(tab.h5)
        index_b = 1
        for link in tab.find_all("a"):
            book_path = top_path + "\\" + str(index_b) +". "+ link.text
            index_b = index_b + 1
            if not os.path.exists(book_path):# 根据课程区分的类别
                os.mkdir(book_path)
            print("            " + link.text + "    " + link.get('href'))
            cls_url = http_pre_path + link.get('href') # 拼接子页面url
            book_page = requests.get(cls_url, timeout=5)# 获取某门课的页面html
            book_page.encoding = book_page.apparent_encoding # 防止页面乱码
            bookSoup = BeautifulSoup(book_page.text, 'html5lib')
            index_c = 1
            for books in bookSoup.find_all("li", 'js_cp'):
                bookName = books.h6.a.text # 课本名称
                booka = books.find("a", class_="btn_type_dl")
                bookHref = booka.get('href') # 课本PDF地址
                bookPath = book_path + "\\" + str(index_c) +". "+bookName + ".pdf" # 拼接课本本地存储路径
                index_c = index_c + 1
                if not os.path.isfile(bookPath):
                    r = requests.get(cls_url + bookHref)# 开始下载
                    with open(bookPath, "wb") as code:
                        code.write(r.content)# 写入本地文件
                    print(bookName + "----" + cls_url + bookHref + "----------已保存")
                print(bookName + "----" + cls_url + bookHref + "----------已存在")

    # for link in soup.find_all('a'):
    #     print(link.text)
    #     print(link.get('href'))


if __name__ == '__main__':
    crawl('http://bp.pep.com.cn/jc/')
