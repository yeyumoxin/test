from testCase import qqEmail_one;
import HTMLTestRunnerCN;
import unittest;


# excase=unittest.defaultTestLoader.discover("../testCase","qqEmail_one.py");
# report=open("../testReport/qqemailResult.html","wb");
# runner=HTMLTestRunnerCN.HTMLTestRunner(stream=report,title="测试",description="描述");
# runner.run(excase);

#打印数据分离的用例报告
excase=unittest.defaultTestLoader.discover("D:\\python\\two\\interfacePractice\\otherPractice","report.py");
report=open("D:\\python\\two\\interfacePractice\\otherPractice\\report.html","wb");
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=report,title="测试",description="描述");
runner.run(excase);