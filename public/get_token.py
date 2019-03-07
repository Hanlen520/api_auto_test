#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
get_pc_token获取pc登录的token
get_app_token获取apptoken
入参暂时写死的
'''

import requests
import json
def get_pc_token():
    #path = path2 = os.path.abspath('..') + '\\test_case_data'+ '\\api_test_dome.xlsx'
    #list_from_excel = read_testData(path)
    #login_url = list_from_excel[1]['接口地址']
    login_url = 'http://192.168.1.246/api/oauth/token'
    login_data = {
    "grant_type": "client_credentials",
    "client_id": "admin",
    "client_secret": "54e95569b3542e8892f906ff6cffe3ec"
    }
    response = requests.post(url=login_url, params=login_data)
#     a = 1
# #获取read_testData返回的list中的元素个数后，遍历调用接口
#     for i in range(0,len(list_from_excel)):
#         login_data = json.loads(list_from_excel[i]['参数'])
#         ogin_url = list_from_excel[i]['接口地址']
#     #s = requests.Session()
#         response = requests.post(url=login_url,params=login_data)
#         print(response.json())
#         a = a + 1
#         print(a)
#         if response.json()['access_token']==list_from_excel[i]['期望']:
#             print('验证ok')
#         else:
#             print('not,ok')

    #print(response.json()['access_token'])

    return response.json()['access_token']


def get_app_token ():
    url ='http://192.168.1.235:8080/v1/member/login?mobile=18621289233&verifycode=593161'
    response = requests.post(url)
    print(response.text)
    return response.json()['responsebody']['token']

if __name__ == '__main__':
    get_app_token()