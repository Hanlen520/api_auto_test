#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import random

def longitude():
    a = random.uniform(120.52,122.11)
    return float(str(a)[:10])

def latitude():
    a = random.uniform(30.42,31.52)
    return float(str(a)[:10])

url = "http://192.168.1.246:8089/v1/park/create"

querystring = {"access_token":"7bdee174-12d4-4f79-948c-ab9dccd4f9a6"}
a = 0
print('开始')
for i in range(100,200):
    a+=1

    title = '批量新增场库_test' + str(i)
    long = longitude()
    #print(long)
    lat = latitude()
    #print(lat)
    payload ={
        "title": title,
        "alias": title,
        "price_standards": "100",
        "temporary_price": "100",
        "monthly_price": "100",
        "release": "平台",
        "manageName": "虹桥艺术中心",
        "province_name": "上海市",
        "city_name": "上海城区",
        "district_name": "嘉定区",
        "manage": "165",
        "release_id": "9999999",
        "province_id": "310000",
        "city_id": "310100",
        "district_id": "310114",
        "address": "迪士尼",
        "longitude": long,
        "latitude": lat,
        "gateways": [],
        "images": [],
        "special_offers": [{
            "type": 1,
            "description": "临停优免"
        }],
        "content": {
            "description": title
        }
    }



    response = requests.request("POST", url, json=payload, params=querystring)

    #print(response.text)
    park_code = response.json()['data']['content']['park_code']
    park_id = response.json()['data']['id']
    url_edit = 'http://192.168.1.246:8089/v1/park/edit'
    data_edit = {
        "id":park_id,
        "park_code":park_code,
        "operation":1}
    #提交
    response_edit = requests.request("POST",url_edit,json = data_edit,params = querystring)

    url_audit  = 'http://192.168.1.246:8089/v1/park/audit'
    data_audit = {
        "operation":0,
        "id":park_id
    }
    #审核
    response_duait = requests.request("POST",url_audit,json = data_audit,params = querystring)
    #上架
    url_add = 'http://192.168.1.246:8089/v1/park/Shelves'
    data_add = {
        "park_code": park_code,
        "status":"1"
    }
    response_duait = requests.request("POST",url_add,json = data_add,params = querystring)


print('新建%s个场库'%a)