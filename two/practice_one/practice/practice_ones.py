# #发邮件
# import smtplib;
# from email.mime.text import MIMEText;
# from email.header import Header;
# from email.mime.multipart import MIMEMultipart;
#
# # meg=MIMEText("<html><h1>测试通过</h1></html>","html","utf-8");
# # meg["Subject"]=Header("443887994@qq.com","utf-8");
# # smtp=smtplib.SMTP_SSL("smtp.qq.com","465");
# # smtp.login("443887994@qq.com","lyiydxwbexhfbhci");
# # smtp.sendmail("443887994@qq.com","2386145389@qq.com",meg.as_string());
# # smtp.connect("smtp.qq.com");
# # smtp.quit();
#
# #设置邮件类型
# msgRoot=MIMEMultipart("related");
# #邮件主题
# msgRoot["Subject"]="自动化测试报告";
# #获取附件
# att=MIMEText(open("D:\\python\\two\\testReport\\qqemailResult.html","rb").read(),"base64","utf-8");
# #文件类型
# att["Content-Type"] = 'application/octet-stream';
# #设置默认文件名
# att["Content-Disposition"] = 'attachment; filename="result.html"';
# #读取附件
# msgRoot.attach(att);
# #开启
# smtp=smtplib.SMTP_SSL("smtp.qq.com","465");
# smtp.login("443887994@qq.com","lyiydxwbexhfbhci");
# smtp.sendmail("443887994@qq.com","2386145389@qq.com",msgRoot.as_string());
# smtp.connect("smtp.qq.com");
# smtp.quit();


#使用qq邮箱发送测试报告
import smtplib;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;

#发件人
sender="443887994@qq.com";
port=465;
#收信人
received="2386145389@qq.com";
#邮箱服务器
smtpServer="smtp.qq.com";
#授权码
autoCode="lyiydxwbexhfbhci";
#邮件类型
msgRoot=MIMEMultipart("related");
#邮件主题
msgRoot["Subject"]="自动化测试报告";
#构建附件
att=MIMEText(open("D:\\python\\two\\testReport\\qqemailResult.html","rb").read(),"base64","utf-8");
att["Content-Type"]="application/octer-stream";
att["Content-Disposition"]="attachment;filename='result.html'";
msgRoot.attach(att);
smtp=smtplib.SMTP_SSL(smtpServer,port);
#发件人邮箱，授权码
smtp.login(sender,autoCode);
#发件人，收件人，msgroot转为string
smtp.sendmail(sender,received,msgRoot.as_string());
#服务器地址
smtp.connect(smtpServer);
#关闭服务
smtp.quit();

