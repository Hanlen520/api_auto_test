#!/usr/bin/python
# -*- coding:utf-8 -*-

from public import request_api,read_excel
import unittest,os,time

class test_dome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始测试')
        try:
            cls.list_from_excel = read_excel.read_excel(os.path.abspath('..') + '\\test_case_data\\api_test_dome.xlsx')
        except:
            cls.list_from_excel = read_excel.read_excel(os.path.abspath('.') + '\\test_case_data\\api_test_dome.xlsx')
        #print(cls.list_from_excel)

    def test_one(self):
        print('第一个case')
        resp = request_api.request_api(self.list_from_excel,0,1)
        self.assertEqual(200, resp[0])
        #print('测试通过')

    def test_two(self):
        print('第二个case')
        resp = request_api.request_api(self.list_from_excel, 2, 3)

        self.assertEqual(200, resp[0])
        #print('测试通过')
    # def test_thir(self):
    #     print('第三个case')
    def test_third(self):
        print('第三个case')
        resp = request_api.request_api(self.list_from_excel, 3, 4)

        self.assertEqual(200, resp[0])
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('测试结束')


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(test_dome)
    #suite.addTest(test_dome(test_two))
    #
    unittest.TextTestRunner().run(suite)