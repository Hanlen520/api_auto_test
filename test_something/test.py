#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# import random
#
#
# def longitude():
#     a = random.uniform(120.52,122.11)
#     return float(str(a)[:10])
# for i in range(3,7):
#     a = longitude()
#     print(a)



# import os
#
# a = os.path.join(os.path.abspath('..'),'test_case_data','api_test_dome.xlsx')
# print(a)

# from public import HTMLTestRunner
'CREATE TABLE states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, state CHAR(25), population INT(9));'
'INSERT INTO states (id, state, population) VALUES (NULL, "Alabama", "4822023");'

import pymysql
import time
def sql_check(sql=None,params=None):
    '''

    :param sql:
    :param params:
    :return: resluts:
    '''
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='199211',
        db='test0310',
        charset='utf8'
    )
    cursor = connect.cursor()
    cursor.execute(sql,params)
    resluts = cursor.fetchall()
    print('连接成功，等待5s')
    time.sleep(5)
    print(resluts)
    cursor.close()
    print('已关闭')
    #print(resluts)


if __name__ =='__main__':
    # sql ='INSERT INTO states (id, state, population) VALUES (NULL, "Alabama", "4822023");'
    # sql_1 = 'select * from states'
    # sql_check(sql_1)

    a = 20*20+50*16+10*5+50*1#炫豆1300
    b = 16*3+20+5+50#活跃度123
    c=28#余额28
    print(b)