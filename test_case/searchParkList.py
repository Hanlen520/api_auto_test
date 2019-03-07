#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json

url = "http://192.168.1.231:8081/v1/park/searchParkList"

querystring = {"bookable":"","distance":"5000","kw":"车位","latitude":"31.21694","longitude":"121.421585","off":"","page":"1","pageSize":"10","sortType":"1","type":"1"}

headers = {
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cache-Control': "no-cache",
    'Postman-Token': "2817b76d-7454-4f29-b8f0-1fbf65329540"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(json.loads(response.text))