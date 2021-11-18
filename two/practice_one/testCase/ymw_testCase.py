#易买网登录用例
from selenium import webdriver;
import time;
import unittest;
from selenium.webdriver.common.by import By


class ymw():
    def __init__(self,driver):
        self.driver=driver;

    # 登录
    def login(self,name,pwd):
        try:
            self.driver.get("http://localhost:8080/EasyBuy/Login?action=toLogin");
            time.sleep(2);
            self.driver.find_element("id","loginName").send_keys(name);
            time.sleep(1);
            self.driver.find_element("id","password").send_keys(pwd);
            time.sleep(1);
            self.driver.find_element(By.CSS_SELECTOR,"body > div.log_bg > div.login > div.log_c > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input").click();
        except Exception as e:
            print(e);
        finally:
            print("执行完成");
    #搜索
    def search(self,value):
        self.driver.get("http://localhost:8080/EasyBuy/Home?action=index");
        time.sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"body > div.top > div.search > form > input.s_ipt").send_keys(value);
        time.sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"body > div.top > div.search > form > input.s_btn").click();

#封装用例
class ymwTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.maximize_window();

    def test_one(self):
        ymw(self.driver).login("admin","123456");

    def test_two(self):
        ymw(self.driver).search("香水");

    def tearDown(self):
        time.sleep(5);
        self.driver.quit();

if __name__ == '__main__':
    testunit = unittest.TestSuite();
    testunit.addTest(ymwTestCase("test_one"));
    unittest.TextTestRunner().run(testunit);