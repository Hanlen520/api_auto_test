#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


list_code_1 = ['pcAE622jY1WX43Koz0','9h6mqIt2hZCoxCcT57','5MD5p4zprofa07Isw8','EWvv5WrSgf3m75UE3w','72170C948YO72CQU2A',
             'Dy240WgieVcWn25l31','b5Y6u86F2XLhkQJ89C','h8zwi1558L5ffS45dy','297hT5fGvoud482Jac',
             '7X85f41N68BR7Yv80i','14pY360t047Od5G2dR','A1718927JpU4SZO675']
list_code = ['pcAE622jY1WX43Koz0','9h6mqIt2hZCoxCcT57','5MD5p4zprofa07Isw8','EWvv5WrSgf3m75UE3w','72170C948YO72CQU2A','A1718927JpU4SZO675']
for code in list_code:
    url = 'https://xapi.flashparking.cn/v1/moveCarBycode/passerby/getVirtualMobile?code=%s'%code
    print(url)
    resp = requests.post(url=url, verify=False)
    time.sleep(1)
    print(resp.json()['responsebody']['contactNumber'],time.ctime())


# url_1 = 'https://xapi.flashparking.cn/v1/moveCarBycode/passerby/getVirtualMobile?code=pcAE622jY1WX43Koz0'
#
# resp_1 = requests.post(url=url_1,verify=False)
#
# print(resp_1.text)