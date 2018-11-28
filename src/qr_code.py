# coding:utf8
# author:jans
# desc: 生成二维码
# 安装二维码模块： pip3 install qrcode
import qrcode
#a = qrcode.make("https://www.baidu.com")
#a.save('baidu.png')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_Q,
    box_size=4,
    border=2
)
qr.add_data("https://www.baidu.com")
qr.make(fit=True)
img = qr.make_image(fill_color='yellow',back_color='blue')
img.save('baidu2.png')