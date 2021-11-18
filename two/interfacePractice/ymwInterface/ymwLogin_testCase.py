#易买网登录接口封装
import unittest
import requests;
import json;

class ymwLogin(unittest.TestCase):
    def test_one(self):
        loginurl="http://localhost:8080/EasyBuy/Login";
        loginPrams="loginName=admin&password=123456&action=login";
        loginreq=requests.request("post",loginurl,params=loginPrams);
        print(json.dumps(loginreq.json(),indent=4,ensure_ascii=False));
        self.assertEqual(1,loginreq.json()["status"]);
        self.assertIn("登陆成功",loginreq.text);
        self.assertTrue("操作成功" in loginreq.text);

if __name__ == '__main__':
    unittest.main();
