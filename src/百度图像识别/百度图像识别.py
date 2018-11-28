# -*- coding:utf-8 -*-

# import 百度AI图片识别
from aip import AipImageCensor

""" 你的 APPID AK SK """

# APP_ID = '你的 App ID'

# API_KEY = '你的 Api Key'

# SECRET_KEY = '你的 Secret Key'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)


# 读取图片

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

img = get_file_content('E://work//baiduaudio//zhengzhi1.jpg')

# 调用图像审核接口
result = client.imageCensorUserDefined(img)

# 如果图片是url调用如下

# result = client.imageCensorUserDefined('http://www.domain.com/image.jpg')

# 获取返回识别结果 一般情况下，结果是一组按照置信度排序的数组

if isinstance(result, dict):
    print(result)

print('###########')

if result.has_key('conclusion'):
    if result['conclusion'] != u'合规':
        print(result['conclusion'])

print('#############')

for data in result['data']:
    print(data['msg'])