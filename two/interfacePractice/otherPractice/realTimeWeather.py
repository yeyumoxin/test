#实时天气接口：
import requests;
import json;
import unittest;

class realTimeWeathers(unittest.TestCase):
    def setUp(self):
        pass;
    def test_one(self):
        wurl="https://tianqiapi.com/api";
        wparams="version=v6&appid=73691227&appsecret=123456";
        wreq=requests.request("get",wurl,params=wparams);
        print(json.dumps(wreq.json(),indent=4,ensure_ascii=False));

        @unittest.skip('不执行此用例')
        # 易买网登录接口
        def test_case02(self):
            url = 'http://localhost:8080/EasyBuy/Login';
            data = 'loginName=admin&password=123456&action=login';
            response = requests.request("post",url, params=data);
            print(json.dumps(response.json(), indent=4, ensure_ascii=False));

if __name__ == '__main__':
    testunit=unittest.TestSuite();
    testunit.addTest(realTimeWeathers("test_one"));
    unittest.TextTestRunner().run(testunit);
