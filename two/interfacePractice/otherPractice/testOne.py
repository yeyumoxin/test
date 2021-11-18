#易买网登录接口测试
import requests;
import json;
import unittest;
import xlrd;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
import time;


class ymw():
    #易买网登录接口
    def loginInterface(self):
        try:
            data=xlrd.open_workbook("C:\\Users\\EDZ\\Desktop\\shujuqudon.xls");
            table=data.sheet_by_name("Sheet1");
            list=[];
            for q in range(0,table.nrows):
                list=table.row_values(q);
                break;
            loginreq=requests.request(list[0],list[1],list[2]);
            print(json.dumps(loginreq.json(),indent=4,ensure_ascii=False));

        except Exception as e:
            print(e);

    @unittest.skip
    #易买网登录功能
    def loginUi(self):
        try:
            data=xlrd.open_workbook("C:\\Users\\EDZ\\Desktop\\shujuqudon.xls");
            table=data.sheet_by_name("Sheet1");
            list=[];
            for q in range(1,table.nrows):
                list=table.row_values();
                break;
            try:
                driver=webdriver.Chrome();
                driver.maximize_window();
                driver.get(list[0]);
                time.sleep(2);
                driver.find_element(By.ID,"loginName").send_keys(list[1]);
                time.sleep(1);
                driver.find_element(By.ID,"password").send_keys(list[2]);
                time.sleep(1);
                driver.find_element(By.CSS_SELECTOR,"body > div.log_bg > div.login > div.log_c > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input").click();
                time.sleep(5);
                driver.quit();
            except Exception as e:
                print(e);
        except Exception as e:
            print(e);

class ymwTestCase(unittest.TestCase):

    def test_ymwone(self):
        ymw().loginInterface();

    def test_ymwtwo(self):
        ymw().loginUi();
