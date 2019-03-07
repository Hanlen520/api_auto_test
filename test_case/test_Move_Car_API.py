#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
挪车码p台接口
后续考虑根据入参，自动查询库中的数据

'''
import requests
import json
import unittest
import os
from public import get_token,read_excel,sql_check,join_url
#读取excel，设置list_from_excel，access_token为全局变量
path =  os.path.abspath('..') + '\\test_case_data'+ '\\api_test_dome.xlsx'
list_from_excel = read_excel.read_excel(path)
access_token = get_token.get_pc_token()
#class RunTest(unittest)
#查询绑定列表
def Test_Bind_list():
    #from urllib.parse import urlencode

    # base_url = 'http://192.168.1.246:8089/v1/moveCarBycode/bind/list'
    base_date = {
        "access_token": access_token,
        "results": 10,
        "page": 1
    }

    #globals()
    for i in range(0,len(list_from_excel)):
        if list_from_excel[i]['接口名'] == '挪车码列表':
            bind_url = list_from_excel[i]['接口地址']
            if list_from_excel[i]['body'] != '':
                bind_body = json.loads(list_from_excel[i]['body'])
                response = requests.post(url=bind_url,json=bind_body,params=base_date)
                if response.status_code == 200:
                    total = response.json()['data']['total']
                    print('验证点:%s通过,查询到：%s'%(list_from_excel[i]['验证点'],total))
                else:
                    print('not,ok')
        else:
            continue
#修改物流状态
def Test_Update_Ship():
    #access_token = get_pc_token.get_pc_token()

    url_params = {
        "access_token": access_token,
        "shipStatus": 1
      }
    for i in range(0,len(list_from_excel)):
        #print(11)
        #print(list_from_excel[i]['接口名'])
        if list_from_excel[i]['接口名']=='更改挪车码物流状态':
            bind_url = join_url.join_url(list_from_excel,i)
            #print(bind_url)
            #ship_param = json.loads(list_from_excel[i]['参数'])
            response = requests.post(bind_url,url_params)
            #print(response.url)
            if response.status_code == 200:

                print('验证点:%s通过' % list_from_excel[i]['验证点'])
            else:
                print('not,ok')
        else:
            continue
#生成实物码
def test_generate():
    for i in range(0,len(list_from_excel)):
        #print(11)
        #print(list_from_excel[i]['接口名'])
        #token = get_token.get_pc_token()
        url_params={}
        url_params['access_token']=access_token
        if list_from_excel[i]['接口名']=='生成实物码':
            bind_url = join_url.join_url(list_from_excel,i)
            #print(bind_url)
            #ship_param = json.loads(list_from_excel[i]['参数'])
            response = requests.post(bind_url,url_params)
            #print(response.url)
            if response.status_code == 200:

                print('验证点:%s通过' % list_from_excel[i]['验证点'])
            else:
                print('not,ok')
        else:
            continue







if __name__ == '__main__':
    Test_Bind_list()
    #update_ship()
    #test_generate()
