#易买网登录接口
# import requests;
# import json;
#
# url="http://localhost:8080/EasyBuy/Login";
# data="loginName=admin&password=123456&action=login";
# rep=requests.request("post",url,params=data);
# print(rep.json());
# print(json.dumps(rep.json(),indent=4,ensure_ascii=False));

import requests;
import json;

url="http://localhost:8080/EasyBuy/Login";
params="loginName=admin&password=123456&action=login";
req=requests.request("post",url,params=params);
print(json.dumps(req.json(),indent=4,ensure_ascii=False));
