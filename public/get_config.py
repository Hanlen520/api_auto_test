#!/usr/bin/python
# -*- coding:utf-8 -*-

import yaml
import os
import pymysql

path = os.path.join(os.path.abspath('..'),'config','config.yml')
with open(path,'r') as file:
    a =file.read()
print(yaml.load(a))
aa =yaml.load(a)
b = aa.get('cont')
print(b)
connect = pymysql.Connect(
    b
)
cursor = connect.cursor()
#cursor.execute(sql, params)
#resluts = cursor.fetchall()
print('连接成功，等待5s')
time.sleep(5)
print(resluts)
cursor.close()
print('已关闭')