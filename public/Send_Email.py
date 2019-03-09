#!/usr/bin/python
# -*- coding:utf-8 -*-

import zmail
import os

class E_mail(object):
    def __init__(self,html,attachment):
        '''
        定义参数/属性f
        :param html:
        :param attachment:
        '''
        self.html = html
        self.attachment = attachment


    def get_from(self):
        #用户后续读取配置文件
        return self.user,self.pasw
    def get_to(self):
        return self.to,

    def send_mail(self):

        server = zmail.server('291139310@qq.com','zevsoaktkwnocadc')
        # day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        # path = os.path.abspath('..') + '\\report\\AutoReport-%s.html'%day
        # with open(path,'r') as f:
        #     html = f.read()

        mail = {
            'subject':'接口自动化测试报告',
            'content_html':self.html,
            'attachments':self.attachment,
            'from':'接口自动化测试'
        }

        server.send_mail(['xuyc@letting.tech'],mail)
        print('ok')



if __name__ == '__main__':
    user='291139310@qq.com'
    pasw='zevsoaktkwnocadc'
    to='xuyc@letting.tech'
    path = os.path.join(os.path.abspath('..'),'report','AutoTestReport-201903100329.html')
    with open(path,'r',encoding='utf-8') as file:
        html = file.read()
    E_mail(html,path).send_mail()
#理解一下 类和方法的 调用
