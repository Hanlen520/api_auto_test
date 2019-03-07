#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
封装
连接数据库
传sql
返回查询结果

'''


import pymysql
def sql_check(sql,params=None):
    '''

    :param sql:
    :param params:
    :return: resluts:
    '''
    connect = pymysql.Connect(
        host='192.168.1.245',
        port=3306,
        user='test2019',
        passwd='123456',
        db='interface',
        charset='utf8'
    )
    cursor = connect.cursor()
    cursor.execute(sql,params)
    resluts = cursor.fetchall()
    #print(resluts)
    return resluts