#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'https://pillow.readthedocs.org/'

__author__ = 'Jans'

from PIL import Image,ImageFilter

#打开图片
img = Image.open('/Users/apple/Pictures/111.png')
########################缩放到50% start############################
#获得图像尺寸
x,y = img.size
print('图像原始大小：%sx%s'%(x,y))
img.thumbnail((x//2,y//2))
#缩放后的大小为
print('缩放后的大小为：%sx%s' % (x//2,y//2))
img.save('/Users/apple/Pictures/222.png')
########################缩放到50% end##############################
########################图像模糊 start############################
img = Image.open('/Users/apple/Pictures/111.png')
# 应用模糊滤镜
img3 = img.filter(ImageFilter.BLUR)
img3.save('/Users/apple/Pictures/333.png')
########################图像模糊 end##############################


