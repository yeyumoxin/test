from selenium import webdriver;
import time;
from practice_one.testCase.baidu_search import bd_search
import unittest;
import HTMLTestRunnerCN;
import xlrd;
from selenium.webdriver.common.by import By

#数据驱动
driver=webdriver.Chrome();
driver.maximize_window();
data=xlrd.open_workbook("D:\\python\\two\\shujuqudon\\table\\shujuqudon.xls");
table=data.sheet_by_name("Sheet1");
list=[];
for q in range(0,table.nrows):
    list=table.row_values(q);
    break;
time.sleep(1);
driver.get(list[0]);
time.sleep(1);
driver.find_element("id",list[1]).send_keys(list[2]);
time.sleep(1);
driver.find_element("id",list[3]).click();
time.sleep(3);
driver.quit();

#执行用例，打印测试报告
# excase=unittest.defaultTestLoader.discover("../testCase/","baidu_search.py");
# report=open("../testReport/result.html","wb");
# runner=HTMLTestRunnerCN.HTMLTestRunner(stream=report,title="测试",description="描述");
# runner.run(excase);

#执行用例
# suite=unittest.TestLoader().loadTestsFromTestCase(bd_search);
# unittest.TextTestRunner(verbosity=1).run(suite);






