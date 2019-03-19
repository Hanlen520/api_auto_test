#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json
import unittest
import os
import re
from public import get_token,read_excel,sql_check,join_url

#读取excel，设置list_from_excel，access_token为全局变量
#path =  os.path.abspath('..') + '\\test_case_data'+ '\\api_test_dome.xlsx'
#list_from_excel = read_excel.read_excel(path)
#pc_token = get_token.get_pc_token()





def request_api(list_from_excel,n=None,m=None):
    '''

    :param list_from_excel:
    :param n: 从第n行开始--行id-1
    :param m: 到第m行--行id-1
    :return:
    '''
    correlation_Dict = {}
    #aa =0
    for i in range(n,m):
        print(i)
        '''
        # url_params = json.loads(list_from_excel[i]['参数'])
        # if url_params !='':
        #    #print(type(url_params))
        #     #print('url_params%s'%url_params)
        #     print(1)
        #     url_params_1 = list_from_excel[i]['参数']
        #     for value in correlation_keys:
        #         print(2)
        #
        #         if url_params_1.find(value)>0:
        #             print(3)
        #             url_params_1 = url_params_1.replace(value, str(correlation_keys[value]))
        #             #print(rl_params)
        #             url_params = json.dumps(json.loads(url_params_1), indent=2, ensure_ascii=False)
        #             print(url_params)
        #             #url_params['access_token'] =pc_token
        #         # else:
        #         #     print(4)
        #         #     url_params = json.loads(list_from_excel[i]['参数'])
        #         #     print(type(url_params))
        # else:
        #     url_params=None
        '''
        #aa+=1
        #print(aa)
        url_params = read_excel.correlation_keys(list_from_excel,i,correlation_Dict)
        #print('入参:%s,格式：%s' % (url_params, type(url_params)))

        requests_url = join_url.join_url(list_from_excel,i,correlation_Dict)
        #print(list_from_excel[i]['body'])

        json_body = read_excel.correlation_body(list_from_excel,i,correlation_Dict)
        #print(requests_url,url_params,json_body)
        method = list_from_excel[i]['接口类型']
        #response = requests.post(url=requests_url,params=url_params,json=json_body)
        resp = API(list_from_excel,i,method=method,url=requests_url,params=url_params,json=json_body)

        #print('返回的值：%s'% (resp,))
        #提取关联参数
        resp1=resp[1]
        if list_from_excel[i]['关联参数'] != '':
            corr = list_from_excel[i]['关联参数'].split('=')
            correlation_Dict = read_excel.get_corr(corr, resp1, correlation_Dict)
        else:
            pass
    return resp
    #print(resp)

        #print(response.url)
        #resp = response.json()
        #return response.status_code
        # if response.status_code == 200:
        #     print('验证点:%s通过' % list_from_excel[i]['验证点'])
        # else:
        #     print('not,ok,%s'%resp)




        #print(resp)

#封装接口调用
def API(list_from_excel,i,method,url,params,json=None):
    try:
        if method =='post':
            try:
                resp = requests.post(url=url,params=params,json=json)
                if resp.status_code == 200:
                    print('验证点:%s==通过' % list_from_excel[i]['验证点'])
                else:
                    print('验证点:%s==not,ok---%s' % (list_from_excel[i]['验证点'], resp.json()))
                return resp.status_code, resp.json()
            except Exception as ee:
                print('调用失败,%s'%ee)
        elif method == 'get':
            try:
                resp = requests.get(url=url,params=params)
                if resp.status_code == 200:
                    print('验证点:%s==通过' % list_from_excel[i]['验证点'])
                else:
                    print('验证点:%s,not,ok,%s' % (list_from_excel[i]['验证点'],resp.json()))
                return resp.status_code,resp.json()
            except Exception as eee:
                print('调用失败，%s'%eee)
    except Exception as e :
        print('格式错误，%s'%e)





if __name__ == '__main__':
    path = os.path.abspath('..') + '\\test_case_data' + '\\api_test_dome.xlsx'
    list_from_excel = read_excel.read_excel(path)
    #print(len(list_from_excel))
    #print(list_from_excel[14])
    # for i in range(12,15):
    #     print(i)
    a=request_api(list_from_excel,12,16)
    print(a)