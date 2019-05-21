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
def format_list(re):
    #re = sql_check(sql)
    a = len(re)
    b = []
    for i in range(0, a):
        aa = re[i][0]
        b.append(aa)
    return b


if __name__ == '__main__':
    sql = "select a.entry_id from ugc_entry a  where a.m_id='43' and a.update_time >=date('2019-05-20')order by create_time desc ;"
    re = sql_check(sql)
    a = len(re)
    b = []
    for i in range(0,a):
        aa = re[i][0]
        b.append(aa)
    print(b)