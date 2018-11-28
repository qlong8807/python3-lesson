#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

from xml.parsers.expat import ParserCreate

class DefaultSAXHandler(object):
    def start_element(self,name,attrs):
        print('sax start_element:%s,attrs:%s' % (name,str(attrs)))
    def char_data(self,data):
        print('sax char_data:%s'%data)
    def end_element(self,name):
        print('sax end_element:%s' % name)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="href1">Java</a></li>
    <li><a href="href2">Python</a></li>
</ol>
'''

handler = DefaultSAXHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)