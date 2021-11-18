#qq邮箱登录
from selenium import webdriver;
from time import sleep;
import unittest;

class qqemaillogin():
    def __init__(self,driver):
        self.driver=driver;

    def login(self,name,pwd):
        sleep(1);
        self.driver.switch_to.frame("login_frame");
        sleep(1);
        self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click();
        sleep(1);
        self.driver.find_element_by_id("u").send_keys(name);  # 账号框
        sleep(1);
        self.driver.find_element_by_id("p").send_keys(pwd);  # 密码框
        sleep(1);
        self.driver.find_element_by_id("login_button").click();

class qqemail(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.maximize_window();
        self.driver.get("http://mail.qq.com");

    def test_one(self):
        qqemaillogin(self.driver).login("2386145389","");

    def tearDown(self):
        sleep(5);
        self.driver.quit();

if __name__ == '__main__':
    # unittest.main();

    suite=unittest.TestLoader().loadTestsFromTestCase(qqemail);
    unittest.TextTestRunner(verbosity=1).run(suite);
