#qq邮箱,封装,百度搜索，登录，发邮件
import unittest;
from selenium import webdriver;
from time import sleep;

#登录类
class qqlogin():
    def __init__(self,driver):
        self.driver=driver;

    def login(self,name,pwd):
        # 切换frame，点击账号密码登录
        sleep(2);
        self.driver.switch_to.frame("login_frame");
        self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click();
        # 登录
        sleep(2);
        self.driver.find_element_by_id("u").send_keys(name);  # 账号框
        sleep(1);
        self.driver.find_element_by_id("p").send_keys(pwd);  # 密码框
        sleep(1);
        self.driver.find_element_by_id("login_button").click();#登录按钮

#写信
class qqwrite_letters():
    def __init__(self,driver):
        self.driver=driver;

    def weite_letters(self,addressee,theme):
        # 点击写信
        sleep(1);
        self.driver.find_element_by_id("composebtn").click();
        # 切换frame，输入收件人
        sleep(1);
        self.driver.switch_to.frame("mainFrame");
        self.driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys(addressee);
        # 输入主题
        sleep(1);
        self.driver.find_element_by_id("subject").send_keys(theme);
        #输入正文
        sleep(1);
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/form[2]/div[2]/div[7]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/iframe'));
        self.driver.find_element_by_css_selector('body > div').send_keys("hello world");
        # 点击发送
        sleep(1);
        self.driver.switch_to.parent_frame();
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click();

class qqemail(unittest.TestCase):
    #初始化
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.maximize_window();
        # 访问百度
        self.driver.get("https://www.baidu.com");
    #执行测试
    def test_one(self):
        #输入搜索内容，点击搜索
        sleep(2);
        self.driver.find_element_by_id("kw").send_keys("qq邮箱");
        self.driver.find_element_by_id("su").click();
        #点击搜索结果
        sleep(2);
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click();
        #进入新打开的页面
        sleep(2);
        self.driver.switch_to.window(self.driver.window_handles[-1]);

        #调用登录
        qqlogin(self.driver).login("2386145389","0902xihuan0111");
        #调用写信
        qqwrite_letters(self.driver).weite_letters("2386145389@qq.com","你好！");
    #结束
    def teardown(self):
        # 结束
        sleep(5);
        self.driver.quit();

if __name__ == '__main__':
    unittest.main();
