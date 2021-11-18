#jwt获取token，登录，上传文件
# import requests;
# import json;
# import jsonpath;
#
# #获取token
# url="http://localhost:8000/login";
# data={
#     "username":"admin",
#     "password":"admin"
# };
# req=requests.request("post",url,params=data);
# print(jsonpath.jsonpath(req.json(),"$..token")[0]);
#
# #使用获取的token登录
# loginurl="http://localhost:8000/auth/hello";
# #token="Bearer"+jsonpath.jsonpath(req.json(),"$..token")[0];
# token = "Bearer " + jsonpath.jsonpath(req.json(), "$..token")[0]
# print(token);
# headers={
#     "Authorization":token
# };
# reqs=requests.get(loginurl,headers=headers);
# print(json.dumps(reqs.json(),indent=4,ensure_ascii=False));
#
# #上传文件
# pushurl="http://httpbin.org/post";
# file=open("C:\\Users\\EDZ\\Desktop\\test.docx");
# files={
#     "file":file
# };
# reqt=requests.request("post",pushurl,files=files);
# print(reqt.json());
# print(json.dumps(reqt.json(),indent=4,ensure_ascii=False));

import requests;
import json;
import jsonpath;

#获取token
tokenurl="http://localhost:8000/login";
tokenParams={
    "username":"admin",
    "password":"admin"
};
tokenreq=requests.request("post",tokenurl,params=tokenParams);
print(json.dumps(tokenreq.json(),indent=4,ensure_ascii=False));

#使用获取的token登录
loginurl="http://localhost:8000/auth/hello";
loginToken="Bearer "+jsonpath.jsonpath(tokenreq.json(),"$..token")[0];
loginHeaders={
    "Authorization":loginToken
};
loginreq=requests.request("get",loginurl,headers=loginHeaders);
print(json.dumps(loginreq.json(),indent=4,ensure_ascii=False));

#上传文件
pushurl="http://httpbin.org/post";
file=open("C:\\Users\\EDZ\\Desktop\\test.docx");
files={
    "file":file
};
pushreq=requests.request("post",pushurl,files=files);
print(json.dumps(pushreq.json(),indent=4,ensure_ascii=False));

