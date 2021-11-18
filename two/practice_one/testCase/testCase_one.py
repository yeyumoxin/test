#百度页面
from selenium import webdriver;
from time import sleep;
import unittest;
from selenium.webdriver import ActionChains;
from selenium.webdriver.common.by import By


class baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.maximize_window();

    def test_one(self):
        self.driver.get("https://www.baidu.com");
        self.driver.find_element("id","s-usersetting-top").click();
        sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"#s-user-setting-menu > div > a.setpref").click();
        sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"#wrapper > div.bdlayer.s-isindex-wrap.new-pmd.pfpanel > div > div > ul > li:nth-child(2)").click();
        sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"#adv-setting-gpc > div > div.c-select-selection > i.c-icon.c-select-arrow").click()
        sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"#adv-setting-gpc > div > div.c-select-dropdown > div.c-select-dropdown-list > p:nth-child(5)").click();

    def test_two(self):
        self.driver.get("https://www.baidu.com");
        self.driver.find_element("id","s-usersetting-top").click();
        sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"#s-user-setting-menu > div > a.setpref").click();
        sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"#wrapper > div.bdlayer.s-isindex-wrap.new-pmd.pfpanel > div > div > ul > li:nth-child(2)").click();
        sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"#adv-setting-gpc > div > div.c-select-selection > i.c-icon.c-select-arrow").click()
        sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"#adv-setting-gpc > div > div.c-select-dropdown > div.c-select-dropdown-list > p:nth-child(5)").click();

    def test_three(self):
        self.driver.get("https://www.baidu.com");
        self.driver.find_element("id","s-usersetting-top").click();
        sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"#s-user-setting-menu > div > a.setpref").click();
        sleep(2);
        self.driver.find_element(By.CSS_SELECTOR,"#wrapper > div.bdlayer.s-isindex-wrap.new-pmd.pfpanel > div > div > ul > li:nth-child(2)").click();
        sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"#adv-setting-gpc > div > div.c-select-selection > i.c-icon.c-select-arrow").click()
        sleep(1);
        self.driver.find_element(By.CSS_SELECTOR,"#adv-setting-gpc > div > div.c-select-dropdown > div.c-select-dropdown-list > p:nth-child(5)").click();

    def tearDown(self):
        sleep(5);
        self.driver.quit();

if __name__ == '__main__':
    unittest.TestCase();
