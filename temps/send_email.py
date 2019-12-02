#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-02 14:45
# software: PyCharm

# SMTP协议也是一个建立在TCP提供的可靠数据传输服务的基础上的应用级协议

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import urllib.parse
import http.client
import json


def eemail():
    mesg = MIMEMultipart()

    sender = 'ldjwyyx@163.com'
    receivers = ['865479851@qq.com']
    text_content = MIMEText('python发送邮件-详见附件', 'plain', 'utf-8')
    mesg['From'] = Header('是我', 'utf-8')
    mesg['To'] = Header('给他', 'utf-8')
    mesg['Subject'] = Header('python发邮件', 'utf-8')
    mesg.attach(text_content)

    with open('/Users/finup/Desktop/upload.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=upload-data.xlsx'
        mesg.attach(xls)

    with open('/Users/finup/Desktop/1.png', 'rb') as f:
        img = MIMEText(f.read(), 'base64', 'utf-8')
        img['Content-Type'] = 'image/png'
        img['Content-Disposition'] = 'attachment; filename=1.png'
        mesg.attach(img)

    smtp = SMTP('smtp.163.com')
    smtp.login(sender, 'wy1989-10-26')
    smtp.sendmail(sender, receivers, mesg.as_string())
    smtp.quit()
    print('邮件已发送')


def short_mesg():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    params = urllib.parse.urlencode({
        'account': 'C85715576',
        'password': '3ccfa9aad2ae687e2fa6ef3108213e65',
        'content': '您的验证码是：55677。请不要把验证码泄露给其他人。',
        'mobile': '18810936553',
        'format': 'json'
    })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    res = conn.getresponse().read().decode('utf-8')
    print(json.loads(res))
    conn.close()


if __name__ == '__main__':
    # eemail()
    short_mesg()

