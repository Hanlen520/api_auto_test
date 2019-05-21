#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from public.sql_check import format_list,sql_check
import pymysql

check_url = 'http://192.168.1.246:8089/v1/ugc/checkEntry?access_token=fad16f04-6b63-41f7-b221-b7380e17defe'
sql = "select a.entry_id from ugc_entry a  where a.m_id='43' and a.update_time >=date('2019-05-20')order by create_time desc ;"
re = sql_check(sql)

entryId_list=format_list(re)

for i in entryId_list:

    check_json = {
      "cause": "11111",
      "entryId": i,
      "num": 3
    }# 审核参数,1,审核通过,2,驳回,3,采纳

    resp = requests.post(url=check_url,json=check_json)

    a = resp.json()
    print(a)
