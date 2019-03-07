#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest,os,time
from test_case.test_dome import test_dome
import HTMLTestRunner
from public.Send_Email import send_mail
#test_dome()
#组装测试用例并执行，调用HTMLTestRunner生成html报告
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_dome))#test_dome为需要执行的测试案例，也可同事执行多个.py文件
#suite.addTest(test_dome('test_two'))
day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
path = os.getcwd() + '\\report\\AutoTestReport-%s.html'%day
f = open(path,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='第一个接口测试报告',description='详细信息')
runner.run(suite)
f.close()
#执行完成发送邮件
with open(path,'r',encoding='utf-8') as file:
    html = file.read()
send_mail(html,path)
#print(html)

#unittest.TextTestRunner().run(suite)
