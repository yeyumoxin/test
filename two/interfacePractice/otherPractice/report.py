#数据驱动和打印报告

import unittest
from selenium import webdriver;
import time;
import HTMLTestRunnerCN;
import json;
import xlrd;
import requests;


class test():
    def testone(self):
        database=xlrd.open_workbook("C:\\Users\\EDZ\\Desktop\\shujuqudon.xls");
        table=database.sheet_by_name("Sheet1");
        list=[];
        for q in range(0,table.nrows):
            list=table.row_values(q);
            break;
        loginreq=requests.request("post",list[0],params=list[1]);
        print(json.dumps(loginreq.json(),indent=4,ensure_ascii=False));

class testReports(unittest.TestCase):
    def setUp(self):
        pass
    def test_one(self):
        test().testone();
    def tearDown(self):
        pass





