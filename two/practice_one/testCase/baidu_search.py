#百度搜索
from selenium import webdriver;
import time;
import unittest;
from selenium.webdriver.common.by import By

class dianji():
    def __init__(self,driver):
        self.driver=driver;

    def test_one(self):
        self.driver.get("https://www.baidu.com");
        time.sleep(3);
        self.driver.find_element(By.CSS_SELECTOR,"#s-top-left > a:nth-child(1)").click();


class bd_search(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.maximize_window();
        self.driver.get("https://www.baidu.com");

    def test_one(self):
        self.driver.find_element(By.CSS_SELECTOR,"#s-top-left > a:nth-child(1)").click();

    def test_two(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(2)").click();

    def test_three(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(3)").click();

    def test_four(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(4)").click();

    def tearDown(self):
        time.sleep(5);
        self.driver.quit();

if __name__ == '__main__':
    unittest.TestCase();