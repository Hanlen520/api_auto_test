#!/usr/bin/python
# -*- coding:utf-8 -*-

import zmail
import os
def send_mail(html,attachment):
    server = zmail.server('291139310@qq.com','zevsoaktkwnocadc')
    # day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # path = os.path.abspath('..') + '\\report\\AutoReport-%s.html'%day
    # with open(path,'r') as f:
    #     html = f.read()

    mail = {
        'subject':'接口自动化测试报告',
        'content_html':html,
        'attachments':attachment,
        'from':'接口自动化测试'
    }

    server.send_mail(['xuyc@letting.tech'],mail)