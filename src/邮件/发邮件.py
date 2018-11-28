#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'当前文档注释'

__author__ = 'Jans'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

'''
把该方法返回的msg按照正常流程发送出去即可。
'''
def get_attach_msg(from_addr,to_addr):
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    # 邮件正文是MIMEText。文本plain和网页HTML可以同时存在。
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))#这个是带附件的text邮件
    # msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    #                     '<p><img src="cid:0"></p>' +
    #                     '</body></html>', 'html', 'utf-8'))#这个是带附件的HTML邮件，可以把附件的图片放到邮件正文中。

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('/Users/apple/Pictures/111.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='test.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
        return msg

# from_addr = input('From: ')
from_addr = 'jans_test@163.com'
password = ''
to_addr = 'abserver@qq.com'
smtp_server = 'smtp.163.com'#smtp.163.com

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')#HTML邮件和文本邮件只有这里有区别，2个参数不同
msg = MIMEText('<html><body><h1>Hello</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

msg2 = get_attach_msg(from_addr,to_addr)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
# server.sendmail(from_addr, [to_addr], msg2.as_string())
server.quit()
