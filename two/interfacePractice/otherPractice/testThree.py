#定时，发邮件
import os;
import time;
import smtplib;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from email.header import Header;
import xlrd;

#定时
while 1:
    try:
        nowTime=time.strftime("%H:%M");
        if nowTime=="20:04":
            os.chdir("D:\\python\\two\\interfacePractice\\otherPractice");
            os.system("python testTwo.py");
            time.sleep(3);

            #数据分离,获取数据
            try:
               data=xlrd.open_workbook("C:\\Users\\EDZ\\Desktop\\shujuqudon.xls");
               table=data.sheet_by_name("Sheet1");
               list=[];
               for q in range(2,table.nrows):
                   list=table.row_values(q);
                   break;
            except:
                print("获取发邮件数据错误");
            # 发邮件
            try:
                sender=list[0];
                port = int(list[1]);
                received=list[2];
                smtpServer=list[3];
                autoCode=list[4];
                msgRoot=MIMEMultipart("related");
                msgRoot["Subject"]="自动化测试报告";
                att=MIMEText(open("D:\\python\\two\\interfacePractice\\otherPractice\\report.html","rb").read(),"base64","utf-8");
                att["Content-Type"] = "application/octer-stream";
                att["Content-Disposition"] = "attachment;filename='result.html'";
                msgRoot.attach(att);
                smtp = smtplib.SMTP_SSL(smtpServer, port);
                smtp.login(sender,autoCode);
                smtp.sendmail(sender,received,msgRoot.as_string());
                smtp.connect(smtpServer);
                smtp.quit();
                print("完成，邮件已发送");
            except:
                print("发邮件错误");
            break;
        else:
            time.sleep(3);
            print(nowTime);
    except:
        print("定时错误");

