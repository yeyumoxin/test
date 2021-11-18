#定时运行
# import os;
# import time;
#
# while 1:
#     now_time=time.strftime("%H:%M");
#     if now_time=="15:17" or now_time=="20:00":
#         os.chdir("D:\\python\\two\\testCase");
#         os.system("python qqEmail_one.py");
#         print("运行完成");
#         break;
#     else:
#         time.sleep(3);
#         print(now_time);

#定时运行测试用例，打印测试报告，发送邮件
import os;
import time;
import smtplib;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from email.header import Header;

#定时打印
while 1:
    try:
        nowTime=time.strftime("%H:%M");
        if nowTime=="19:57" or nowTime=="20:00":
            os.chdir("D:\\python\\two\\executeTestCase");
            os.system("python practiceTestCase.py");
            time.sleep(5);
            #发邮件
            sender = "443887994@qq.com";
            port = 465;
            received = "2386145389@qq.com";
            smtpServer = "smtp.qq.com";
            autoCode = "lyiydxwbexhfbhci";
            msgRoot=MIMEMultipart("related");
            msgRoot["Subject"]="自动化测试报告";
            att=MIMEText(open("D:\\python\\two\\testReport\\qqemailResult.html","rb").read(),"base64","utf-8");
            att["Content-Type"]="application/octer-stream";
            att["Content-Disposition"]="attachment;filename='result.html'";
            msgRoot.attach(att);
            smtp = smtplib.SMTP_SSL(smtpServer, port);
            smtp.login(sender, autoCode);
            smtp.sendmail(sender, received, msgRoot.as_string());
            smtp.connect(smtpServer);
            smtp.quit();
            print("运行完成,邮件已发送");
            break;
    except Exception as ect:
        #发生错误，发送错误信息邮件
        meg=MIMEText("<html><h1>%s</h1></html>"%ect,"html","utf-8");
        meg["Subject"]=Header("443887994@qq.com","utf-8");
        smtp=smtplib.SMTP_SSL("smtp.qq.com","465");
        smtp.login("443887994@qq.com","lyiydxwbexhfbhci");
        smtp.sendmail("443887994@qq.com","2386145389@qq.com",meg.as_string());
        smtp.connect("smtp.qq.com");
        smtp.quit();
    else:
        time.sleep(3);
        print(nowTime);

