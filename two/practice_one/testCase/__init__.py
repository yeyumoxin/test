from selenium import webdriver;
import time;
from practice_one.testCase.baidu_search import dianji
import unittest;

driver=webdriver.Chrome();
driver.maximize_window();
dianji(driver).test_one();