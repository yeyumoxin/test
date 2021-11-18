#访问百度
from selenium import webdriver;
from time import sleep;
from selenium.webdriver.common.by import By
#需要安装
import xlrd;


driver=webdriver.Chrome();
driver.maximize_window();
#导入文件，要xls后缀
data=xlrd.open_workbook("D:\\python\\two\\shujuqudon\\table\\shujuqudon.xls");
#指定那个表
table=data.sheet_by_name("Sheet1");
list=[];
#循环将第一行的内容传给list
for q in range(0,table.nrows):
    list=table.row_values(q);
    break;
sleep(1);
driver.get(list[0]);
sleep(1);
driver.find_element(By.ID,list[1]).send_keys(list[2]);
sleep(2);
driver.find_element(By.ID,list[3]).click();

list=[];
for q in range(1,table.nrows):
    list=table.row_values(q);
    break;
sleep(1);
driver.find_element(By.CSS_SELECTOR,list[0]).click();
sleep(5);
driver.quit();

