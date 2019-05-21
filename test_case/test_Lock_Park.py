#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest,os,time
from public import request_api,read_excel,sql_check

class test_lock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('test start')
        cls.path = os.path.join(os.path.abspath('..'),'test_case_data','api_test_dome.xlsx')
        cls.ex_list =read_excel.read_excel(cls.path)
        print(cls.ex_list)


    def test_case1(self):
        print('验证申请地锁数据入库是否正确')
        resp = request_api.request_api(self.ex_list,16,18)
        self.sql=self.ex_list[17]['sql']
        relust = sql_check.sql_check(self.sql)
        self.assertIn('人民公园auto_test2',relust[0])

    def test_case2(self):
        print('验证申请地锁列表返回的总数是否与数据库一致')
        resp = request_api.request_api(self.ex_list,18,20)
        self.sql = self.ex_list[19]['sql']
        relust = sql_check.sql_check(self.sql)
        total = resp[1]['responsebody']['total']
        self.assertIn(total,relust[0])

    def test_case3(self):
        print('验证p端地锁申请列表返回的总数是否与数据库一致')

    def test_case4(self):
        print('p端驳回申请，c端删除')


    def test_case5(self):
        print('p端审核通过，c端查看')



    def test_case6(self):
        print('c端发布车位并查看发布的车位详情')


    def test_case7(self):
        print('查看车位列表')


    def test_case8(self):
        print('p端驳回c端发布的车位')


    def test_case9(self):
        print('p端审核通过c端发布的车位')

    def test_case10(self):
        print('')



    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('test over')



if __name__ == '__main__':
    sudio = unittest.main()