#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
拼接url
如：
http://192.168.1.246:8089
/v1/moveCarBycode/bind/updShipStatus/{id}

'''

import os
from public.read_excel import correlation_url
def join_url(list_data,i,correlation_Dict):

    # path = os.path.abspath('..') + '\\test_case_data' + '\\api_test_dome.xlsx'
    #
    # list_data = read_excel.read_excel(path)
    url_key = list_data[i]['url参数']
    #print(list_data,i)
    if url_key == '' :
        return list_data[i]['接口地址']
        #print('返回原url')
    elif url_key.find('$') >= 0 :
        url_key_1 = correlation_url(list_data,i,correlation_Dict)
        url = str(list_data[i]['接口地址']) + '/' +url_key_1
        return url
    else:
        url = str(list_data[i]['接口地址']) +'/'+str(list_data[i]['url参数'])
        #print(url)
        return url
'''
def correlation_keys(list_data,i,correlation_Dict):
    import json
    #correlation_Dict ={}#定义一个空字典，存放关联参数
    #print ('body%s'%type(json.loads(list_data[i]['body'])))
    #print(type(correlation_Dict))
    url_params= json.loads(list_data[i]['参数'])
    if url_params != '' and correlation_Dict !={}:
        # print(type(url_params))
        # print('url_params%s'%url_params)
        print(1)
        url_params_1 = list_data[i]['参数']
        for value in correlation_Dict:
            print(2)
            if url_params_1.find(value) > 0:
                print(3)
                url_params_1 = url_params_1.replace(value, str(correlation_Dict[value]))
                print('url_params_1%s,type:%s'%(url_params_1,type(url_params_1)))
                url_params_2 = json.loads(url_params_1)

                print('url_params_2%s,type:%s'%(url_params_2,type(url_params_2)))
                return url_params_2
                # url_params['access_token'] =pc_token
            else:
                print(4)
                url_params_4 = json.loads(list_from_excel[i]['参数'])
                print(type(url_params_4))
                return url_params_4
    elif url_params!='':
        print(6)
        url_params_3 = json.loads(list_data[i]['参数'])
        return url_params_3

    else:

        print(5)
        return None
'''



if __name__ =='__main__':
    from public import read_excel
    path = os.path.abspath('..') + '\\test_case_data' + '\\api_test_dome.xlsx'
    list_from_excel = read_excel.read_excel(path)
    correlation_Dict={}
    for i in range(0, len(list_from_excel)):
        #join_url(list_from_excel,i)
        a =correlation_keys(list_from_excel,i,correlation_Dict)
        print(a)