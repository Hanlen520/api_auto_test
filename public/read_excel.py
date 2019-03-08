#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
读取excel
将所有行组装为一个list
每个元素都是str类型，入参是json格式的需要使用如下方法转换
json.loads(list[i]['参数'])

'''

import xlrd
import  os,sys
import json
import re

def read_excel(file):
    '''
    传入excel路径
    :param file:
    :return: list
    '''
    data = xlrd.open_workbook(file)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(0)  # one rows data
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                # row[i] = colnames[i] + row[i]
                app[colnames[i]] = row[i]
            list.append(app)
    #print(type(list))

    return list

def correlation_keys(list_data,i,correlation_Dict):
    '''
    替换关联参数
    :param list_data:
    :param i:
    :param correlation_Dict:
    :return:
    '''

    #correlation_Dict ={}#定义一个空字典，存放关联参数
    #print ('body%s'%type(json.loads(list_data[i]['body'])))
    #print(type(correlation_Dict))
    url_params= json.loads(list_data[i]['参数'])
    if url_params != '' and correlation_Dict !={}:
        # print(type(url_params))
        # print('url_params%s'%url_params)
        #print(1)
        url_params_1 = list_data[i]['参数']
        for value in correlation_Dict:
            #print(2)
            if url_params_1.find(value) > 0:
                #print(3)
                url_params_1 = url_params_1.replace(value, str(correlation_Dict[value]))
                #print('url_params_1%s,type:%s'%(url_params_1,type(url_params_1)))
                url_params_2 = json.loads(url_params_1)

                #print('url_params_2%s,type:%s'%(url_params_2,type(url_params_2)))
                return url_params_2
                # url_params['access_token'] =pc_token
            else:
                #print(4)
                url_params_4 = json.loads(list_data[i]['参数'])
                #print(type(url_params_4))
                return url_params_4
    elif url_params!='':
        #print(6)
        url_params_3 = json.loads(list_data[i]['参数'])
        return url_params_3

    else:

        #print(5)
        return None


def correlation_url(list_data,i,correlation_Dict):
    '''
    :param list_data:
    :param i:
    :param correlation_Dict:
    :return: 替换url中的参数
    '''
    url_keys = list_data[i]['url参数']
    if url_keys != '' and correlation_Dict != '':
        url_keys_1 = list_data[i]['url参数']
        for value in correlation_Dict:
            if url_keys_1.find(value) >= 0:
                url_keys_1 =url_keys_1.replace(value,str(correlation_Dict[value]))
                return url_keys_1

    else:
        return

def correlation_body(list_data,i,correlation_Dict):
    '''
    body的参数替换
    :param list_data:
    :param i:
    :param correlation_Dict:
    :return:
    '''
    url_body = list_data[i]['body']
    if url_body != '' and url_body.find('$') >= 0:

        for value in correlation_Dict:
            print(value)
            if url_body.find(value) >= 0:
                # print(3)
                url_body = url_body.replace(value, str(correlation_Dict[value]))
                url_body = json.loads(url_body)
                return url_body

    elif url_body != '' and url_body.find('$') < 0 :
        return json.loads(list_data[i]['body'])
    else:
        return







if __name__ == '__main__':
    path = os.path.abspath('..') + '\\test_case_data\\api_test_dome.xlsx'
    list_from_excel = read_excel(path)
    #print(len(list_from_excel))
    #list_from_excel[0]
    url_keys = list_from_excel[14]['body']
    print(url_keys)
    #url_params={"access_token": "${access_token}", "results": 10, "page": 1}
    correlation_keys = {"${access_token}": "b811dad1-139d-4e5b-980c-650faae93e74","${id}":"75"}
    #print(type(correlation_keys))
    a =correlation_body(list_from_excel,14,correlation_keys)
    print(a)
    print('what fuck')
    # for value in correlation_keys:
    #     a  = url_keys.find(value)
    #     print(value,a)
    #     #print('find:%s'%a)
    #     if url_keys.find(value) >= 0 :
    #         url_keys = url_keys.replace(value, str(correlation_keys[value]))
    #         print('key:%s'%url_keys)
    #     else:
    #         print('meiy')
        #a =json.dumps(json.loads(url_keys),indent=2,ensure_ascii=False)
        #print(a)

        # if tuple(url_params).find(value)>0:
        #     url_params = url_params.replace(value,str(correlation_keys[value]))
        #     print(url_params)
        # else:
        #     print('not,ok')