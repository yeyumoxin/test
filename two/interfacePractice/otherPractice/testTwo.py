#执行testOne，打印报告
import unittest;
import time;
import HTMLTestRunnerCN;

#打印报告：
excase=unittest.defaultTestLoader.discover("D:\\python\\two\\interfacePractice\\otherPractice","testOne.py");
report=open("D:\\python\\two\\interfacePractice\\otherPractice\\report.html","wb");
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=report,title="测试",description="描述");
runner.run(excase);